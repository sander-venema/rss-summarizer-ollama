# 📰 RSS Summarizer with Ollama

An intelligent RSS feed aggregator that uses **Ollama** and **Llama 3.2 3B** to automatically summarize news articles from multiple international sources. Built with FastAPI and featuring a modern, responsive web interface with real-time progress tracking.

![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Ollama](https://img.shields.io/badge/Ollama-Llama%203.2%203B-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🤖 **AI-Powered Summaries**: Uses Llama 3.2 3B via Ollama for intelligent article summarization
- 📏 **Custom Summary Length**: Choose between Short (2-3 sentences), Medium (5-7 sentences), or Long (10-15 sentences)
- 🎨 **Dark/Light Theme**: Toggle between dark and light modes with persistent preference
- 🖼️ **News Source Logos**: Visual identification with favicon/logo for each news source
- 📡 **22 News Sources**: Curated selection of top-tier international news feeds
- ✅ **Selective Processing**: Choose which news sources to summarize with checkboxes
- 🔢 **Configurable Articles**: Select 1-10 articles per feed with live estimate
- 📊 **Real-Time Progress**: Live progress bar with ETA and current article tracking
- 🎯 **Auto-Scroll**: Automatically scrolls to progress bar when summarization starts
- 🎨 **Modern UI**: Clean, responsive interface built with Pico CSS
- 🐳 **Docker Ready**: Fully containerized for easy deployment
- 🔄 **Streaming Updates**: Server-Sent Events for real-time progress updates

## 📋 Supported News Sources

### International News
- BBC News
- Reuters World News
- The Guardian - World
- The New York Times - World
- Associated Press - Top News
- NPR News
- Deutsche Welle - Top Stories
- France 24 - International

### Netherlands
- NOS Nieuws - Politiek
- NOS Nieuws - Buitenland
- NOS Nieuws - Tech
- NOS Nieuws - Algemeen
- NOS Nieuws - Binnenland
- NOS Nieuws - Economie
- NOS Nieuws - Sport
- NOS Nieuws - Cultuur & Media
- NOS Nieuws - Opmerkelijk
- NOS Nieuws - Koningshuis

### Technology
- TechCrunch
- Ars Technica
- The Verge
- Hacker News

## 🚀 Quick Start

### Prerequisites

- [Docker](https://www.docker.com/get-started) and Docker Compose
- [Ollama](https://ollama.ai/) installed and running on your host machine
- Llama 3.2 3B model downloaded

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rss-summarizer-ollama.git
   cd rss-summarizer-ollama
   ```

2. **Install and start Ollama** (if not already installed)
   ```bash
   # On macOS/Linux
   curl -fsSL https://ollama.com/install.sh | sh
   
   # On Windows
   # Download from https://ollama.com/download
   ```

3. **Pull the Llama 3.2 3B model**
   ```bash
   ollama pull llama3.2:3b
   ```

4. **Create environment file**
   ```bash
   cp .env.example .env
   # Edit .env if needed (optional for Ollama-only setup)
   ```

5. **Start the application**
   ```bash
   docker-compose up --build
   ```

6. **Open your browser**
   Navigate to `http://localhost:8000`

## 🎯 Usage

1. **Select News Sources**: Check/uncheck the news sources you want to summarize
2. **Configure Settings**:
   - Choose number of articles per feed (1-10)
   - Select summary length (Short, Medium, or Long)
3. **Toggle Theme**: Click the 🌙/☀️ button in the top-right to switch between dark/light mode
4. **Click "Summarize Selected Feeds"**: Start the summarization process
5. **Watch Progress**: Page auto-scrolls to show real-time progress bar with ETA and current article
6. **Read Summaries**: AI-generated summaries appear with news source logos for easy identification

## 🏗️ Architecture

```
rss-summarizer-ollama/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   └── templates/
│       └── index.html       # Frontend UI
├── rss_feeds.json           # RSS feed configuration
├── requirements.txt         # Python dependencies
├── Dockerfile              # Container definition
├── docker-compose.yml      # Docker Compose config
└── .env                    # Environment variables
```

## 🔧 Configuration

### Adding New RSS Feeds

Edit `rss_feeds.json`:

```json
{
  "name": "Your News Source",
  "url": "https://example.com/rss",
  "category": "International"
}
```

### Environment Variables

Create a `.env` file:

```env
# Optional: Custom Ollama host (default: http://host.docker.internal:11434)
OLLAMA_HOST=http://localhost:11434
```

## 🐳 Docker Configuration

The application uses Docker to ensure consistent deployment across different environments.

### Docker Compose

```yaml
version: '3.8'
services:
  rss-summarizer:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OLLAMA_HOST=http://host.docker.internal:11434
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

### Running Without Docker

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variable**
   ```bash
   export OLLAMA_HOST=http://localhost:11434
   ```

3. **Run the application**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

## 📊 How It Works

1. **Feed Fetching**: Uses `feedparser` to retrieve RSS feeds
2. **Content Extraction**: `trafilatura` extracts clean article text
3. **AI Summarization**: Ollama's Llama 3.2 3B generates concise summaries
4. **Streaming Progress**: Server-Sent Events provide real-time updates
5. **Display**: Results shown in a clean, organized interface

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python 3.13)
- **AI Model**: Llama 3.2 3B via Ollama
- **Frontend**: HTML5, JavaScript, Pico CSS
- **RSS Parsing**: feedparser
- **Content Extraction**: trafilatura
- **Containerization**: Docker & Docker Compose

## 📝 API Endpoints

- `GET /` - Main interface
- `POST /summarize` - Start summarization (returns SSE stream)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for making local LLMs accessible
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework
- [Pico CSS](https://picocss.com/) for the beautiful minimal CSS framework
- All the news organizations providing RSS feeds

## 🐛 Troubleshooting

### Ollama Connection Issues

If you see "Could not connect to Ollama":
- Ensure Ollama is running: `ollama serve`
- Check if the model is downloaded: `ollama list`
- Verify the OLLAMA_HOST environment variable

### Docker Issues

If the container can't reach Ollama:
- On Windows/Mac: Use `host.docker.internal`
- On Linux: Use `--network host` or configure bridge networking

### Slow Summarization

- The Llama 3.2 3B model processes ~10-15 seconds per article
- Consider using a GPU for faster inference
- Reduce the number of articles per feed in the code

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

Made with ❤️ using Ollama and FastAPI

