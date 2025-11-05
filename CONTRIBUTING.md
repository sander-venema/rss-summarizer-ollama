# Contributing to RSS Summarizer Ollama

Thank you for your interest in contributing to RSS Summarizer Ollama! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Your environment (OS, Docker version, Ollama version)
- Screenshots if applicable

### Suggesting Enhancements

We love new ideas! Please open an issue with:
- A clear description of the enhancement
- Why this would be useful
- Possible implementation approach

### Adding New RSS Feeds

To add new RSS feeds:

1. Edit `rss_feeds.json`
2. Add your feed following this format:
   ```json
   {
     "name": "Source Name",
     "url": "https://example.com/rss",
     "category": "Category Name"
   }
   ```
3. Test that the feed works
4. Submit a pull request

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add some feature'`)
6. Push to the branch (`git push origin feature/your-feature-name`)
7. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and small

### Testing

Before submitting a PR:
- Test with Docker: `docker-compose up --build`
- Verify all selected feeds work
- Check the progress bar updates correctly
- Ensure summaries are generated properly

## Development Setup

1. Clone your fork
2. Install dependencies: `pip install -r requirements.txt`
3. Install Ollama and pull the model: `ollama pull llama3.2:3b`
4. Run locally: `uvicorn app.main:app --reload`

## Questions?

Feel free to open an issue for any questions!

Thank you for contributing! 🎉

