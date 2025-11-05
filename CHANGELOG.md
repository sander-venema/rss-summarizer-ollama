# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-11-05

### Added
- **Configurable articles per feed**: Users can now select 1-10 articles per feed via UI input
- **Live estimate display**: Shows total articles and estimated processing time before summarization
- **7 additional NOS feeds**: Algemeen, Binnenland, Economie, Sport, Cultuur & Media, Opmerkelijk, Koningshuis
- **Enhanced progress bar**: Beautiful cyan/blue gradient with shimmer animation and glow effects
- **Pulse animation**: Current article being processed has a pulsing glow effect
- **Mobile access documentation**: Complete guide for accessing the app from phone (MOBIEL_TOEGANG.md)
- **Improved prompt**: Better instruction to Ollama to avoid introductory phrases in summaries

### Changed
- Progress bar height increased from 30px to 40px for better visibility
- Progress bar now features gradient backgrounds and 3D shadow effects
- Progress container has slide-in animation when appearing
- Current article display has enhanced styling with gradient background
- Total RSS feeds increased from 15 to 22 (10 NOS feeds total)

### Fixed
- Summary responses now have clearer prompts to reduce unwanted prefixes

## [1.0.0] - 2025-11-05

### Added
- Initial release of RSS Summarizer with Ollama
- AI-powered article summarization using Llama 3.2 3B via Ollama
- Support for 15+ international news sources
- Real-time progress tracking with ETA
- Server-Sent Events for streaming updates
- Checkbox-based feed selection (all enabled by default)
- Modern, responsive UI with Pico CSS
- Docker and Docker Compose support
- Comprehensive logging system
- RSS feed configuration via JSON file

### Features
- **News Sources**:
  - International: BBC, Reuters, Guardian, NYT, AP, NPR, DW, France 24
  - Netherlands: NOS Nieuws (Politiek, Buitenland, Tech, Algemeen, Binnenland, Economie, Sport, Cultuur & Media, Opmerkelijk, Koningshuis)
  - Technology: TechCrunch, Ars Technica, The Verge, Hacker News
- **Progress Tracking**:
  - Real-time progress bar
  - Current article display
  - ETA calculation
  - Article count tracking
- **User Interface**:
  - Select/Deselect all buttons
  - Category-organized feed selection
  - Responsive design
  - Clean article cards with source attribution

### Technical
- FastAPI backend with async support
- Ollama HTTP API integration
- Trafilatura for content extraction
- Feedparser for RSS parsing
- Docker containerization with host networking support

## [Unreleased]

### Planned
- [ ] Add more international news sources
- [ ] Support for custom RSS feed URLs
- [ ] Article caching to avoid re-processing
- [ ] Export summaries to PDF/Markdown
- [ ] Scheduled automatic summarization
- [ ] Email digest feature
- [ ] Multi-language support
- [ ] Custom summary length options
- [ ] Article filtering by keywords
- [ ] Dark/light theme toggle

