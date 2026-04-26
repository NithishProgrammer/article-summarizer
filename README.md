📝 Article Summarizer API
An open-source, high-performance FastAPI service that extracts and summarizes content from web articles using Natural Language Processing (NLP).

🚀 Features
Automated Extraction: Pulls main article text while ignoring ads and navigation using BeautifulSoup.

Extractive Summarization: Uses the Luhn Algorithm to identify the most significant sentences.

Customizable Length: Define how many sentences you want in your summary via query parameters.

Built-in Documentation: Interactive API docs via Swagger UI.

🛠️ Tech Stack
Language: Python 3.10+

Framework: FastAPI

NLP Library: Sumy

Data Source: NLTK (Punkt Tokenizer)

Web Scraping: BeautifulSoup4

📦 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/yourusername/article-summarizer.git
cd article-summarizer
Install dependencies:

Bash
pip install fastapi uvicorn beautifulsoup4 requests sumy nltk
Run the server:

Bash
uvicorn main:app --reload
Access the API:

API: http://127.0.0.1:8000

Interactive Docs: http://127.0.0.1:8000/docs

📖 Usage Example
Request:
POST /summarize?url=https://example.com/article&count=3

Response:

JSON
{
  "url": "https://example.com/article",
  "summary": [
    "The first most important sentence extracted from the text.",
    "The second most important sentence that provides context.",
    "The final concluding point of the article."
  ]
}
⚠️ Demerits & Limitations (The "Honest" Section)
As an open-source project, it’s important to acknowledge where the logic currently has room for improvement:

1. Extractive vs. Abstractive
The Issue: This tool uses Extractive summarization (copy-pasting the best sentences). It does not "write" new sentences like ChatGPT (Abstractive).

The Result: The summary might feel slightly "choppy" because sentences are taken out of their original context.

2. The "Paywall" & "Bot Block" Problem
The Issue: Simple requests calls are often blocked by high-security sites (e.g., New York Times) or sites with paywalls.

The Result: Some URLs will return a 403 Forbidden error or only scrape the "Subscribe Now" text.

3. JavaScript-Heavy Sites (SPA)
The Issue: BeautifulSoup only sees the initial HTML. If a site loads its content using React or Vue (like many modern dashboards), the API will find an empty page.

The Result: You might get an empty summary for very modern web apps.

4. Logic Bias (Luhn Algorithm)
The Issue: The Luhn algorithm prioritizes "significant words."

The Result: If an article uses a specific buzzword repeatedly, the summarizer might focus too much on those sentences, even if they aren't the main point.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request to help solve the Demerits listed above—specifically improving the web scraping robustness.
