# GitHub Setup Instructions

Follow these steps to publish your RSS Summarizer to GitHub:

## Step 1: Rename the Directory (Optional but Recommended)

Since the project is now Ollama-based, you may want to rename the directory:

```powershell
# Navigate to the parent directory
cd C:\Users\sande\Desktop

# Rename the directory
Rename-Item -Path "rss-summarizer-gemini" -NewName "rss-summarizer-ollama"

# Navigate into the renamed directory
cd rss-summarizer-ollama
```

## Step 2: Create a GitHub Repository

1. Go to [GitHub](https://github.com) and log in
2. Click the **+** icon in the top right corner
3. Select **New repository**
4. Fill in the details:
   - **Repository name**: `rss-summarizer-ollama`
   - **Description**: `AI-powered RSS feed aggregator using Ollama and Llama 3.2 3B with real-time progress tracking`
   - **Visibility**: Choose Public or Private
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
5. Click **Create repository**

## Step 3: Push to GitHub

After creating the repository, GitHub will show you commands. Use these:

```powershell
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/rss-summarizer-ollama.git

# Rename the default branch to main (if needed)
git branch -M main

# Push your code
git push -u origin main
```

## Step 4: Add Repository Topics (Optional)

On your GitHub repository page:
1. Click the ⚙️ gear icon next to "About"
2. Add topics: `ollama`, `llama`, `rss`, `fastapi`, `ai`, `summarization`, `news-aggregator`, `python`, `docker`
3. Save changes

## Step 5: Enable GitHub Pages (Optional)

If you want to showcase your project:
1. Go to repository **Settings**
2. Scroll to **Pages**
3. Select source branch (usually `main`)
4. Save

## Alternative: Using GitHub CLI

If you have GitHub CLI installed:

```powershell
# Create repository and push in one command
gh repo create rss-summarizer-ollama --public --source=. --remote=origin --push
```

## Verify Your Repository

After pushing, verify:
- ✅ All files are present
- ✅ README.md displays correctly
- ✅ License is recognized
- ✅ .gitignore is working (no .env file should be visible)

## Next Steps

Consider adding:
- **GitHub Actions** for CI/CD
- **Issue templates** for bug reports and feature requests
- **Pull request template**
- **Screenshots** in the README
- **Demo video** or GIF

## Troubleshooting

### Authentication Issues

If you get authentication errors:

```powershell
# Use Personal Access Token
# Go to GitHub Settings > Developer settings > Personal access tokens
# Generate a new token with 'repo' scope
# Use the token as your password when pushing
```

Or configure SSH:

```powershell
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub: Settings > SSH and GPG keys > New SSH key
# Then use SSH URL instead:
git remote set-url origin git@github.com:YOUR_USERNAME/rss-summarizer-ollama.git
```

---

**Congratulations!** Your project is now on GitHub! 🎉

