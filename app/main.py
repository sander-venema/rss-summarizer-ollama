# app/main.py
import os
import feedparser
import trafilatura
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import logging
import requests
import json
from typing import List
import asyncio
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load RSS feeds from JSON file
def load_rss_feeds():
    with open('rss_feeds.json', 'r') as f:
        return json.load(f)

RSS_FEEDS = load_rss_feeds()

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


def summarize_ollama(text: str, url: str):
    """Summarize using local Ollama + Llama 3.2 3B Instruct model via HTTP API."""
    logger.info(f"[Ollama] Summarizing {len(text)} chars from {url}")
    prompt = f"Summarize the following news article into 5-10 sentences. Provide only the summary without any introductory phrases like 'Here is a summary' or 'Hier is een samenvatting':\n\n{text}\n\nURL: {url}"

    # Use host.docker.internal to connect to Ollama running on host machine
    # If running locally without Docker, use localhost
    ollama_host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")

    try:
        logger.info(f"[Ollama] Calling Ollama API at {ollama_host}...")
        response = requests.post(
            f"{ollama_host}/api/generate",
            json={
                "model": "llama3.2:3b",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        result = response.json()
        output = result.get("response", "").strip()
        logger.info(f"[Ollama] Got response ({len(output)} chars)")
        return output
    except requests.exceptions.ConnectionError:
        logger.error("[Ollama ERROR] Could not connect to Ollama")
        return "[Ollama error] Could not connect to Ollama. Make sure Ollama is running on your host machine."
    except requests.exceptions.Timeout:
        logger.error("[Ollama ERROR] Request timed out")
        return "[Ollama error] Request timed out - Ollama is taking too long to respond"
    except Exception as e:
        logger.error(f"[Ollama ERROR] {e}", exc_info=True)
        return f"[Ollama error] {str(e)}"
    

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    logger.info("Index page accessed")
    return templates.TemplateResponse("index.html", {"request": request, "articles": [], "feeds": RSS_FEEDS})


@app.post("/summarize")
async def run_summarizer(selected_feeds: List[str] = Form(...), articles_per_feed: int = Form(3)):
    """Stream progress updates while summarizing articles."""

    async def generate_progress():
        articles = []
        selected_feed_list = [f for f in RSS_FEEDS if f['url'] in selected_feeds]

        # Validate articles_per_feed
        max_articles = max(1, min(articles_per_feed, 10))  # Limit between 1 and 10

        # Calculate total articles to process
        total_articles = 0
        for feed in selected_feed_list:
            parsed_feed = feedparser.parse(feed['url'])
            total_articles += min(len(parsed_feed.entries), max_articles)

        processed = 0
        start_time = time.time()

        for feed in selected_feed_list:
            logger.info(f"Fetching feed: {feed['name']} ({feed['url']})")
            parsed_feed = feedparser.parse(feed['url'])

            for entry in parsed_feed.entries[:max_articles]:
                url = entry.link
                title = entry.title

                # Send progress update
                progress_percent = int((processed / total_articles) * 100) if total_articles > 0 else 0
                elapsed = time.time() - start_time
                avg_time_per_article = elapsed / processed if processed > 0 else 0
                remaining_articles = total_articles - processed
                eta_seconds = int(avg_time_per_article * remaining_articles) if processed > 0 else 0

                yield f"data: {json.dumps({'type': 'progress', 'current': processed, 'total': total_articles, 'percent': progress_percent, 'eta': eta_seconds, 'current_article': title, 'current_source': feed['name']})}\n\n"

                logger.info(f"Processing article: {title}")
                downloaded = trafilatura.fetch_url(url)
                content = trafilatura.extract(downloaded) if downloaded else entry.get("summary", "")

                if not content:
                    logger.warning(f"No content found for {url}")
                    summary = "No content found."
                else:
                    summary = summarize_ollama(content, url)

                articles.append({
                    "title": title,
                    "url": url,
                    "summary": summary,
                    "source": feed['name']
                })

                processed += 1

        # Send completion with all articles
        logger.info(f"Completed summarization. Total articles: {len(articles)}")
        yield f"data: {json.dumps({'type': 'complete', 'articles': articles})}\n\n"

    return StreamingResponse(generate_progress(), media_type="text/event-stream")


@app.get("/results", response_class=HTMLResponse)
async def show_results(request: Request):
    """Show results page after summarization."""
    return templates.TemplateResponse("index.html", {"request": request, "articles": [], "feeds": RSS_FEEDS})
