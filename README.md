# 📝 Article Summarizer API

An open-source, high-performance FastAPI service that extracts and summarizes content from web articles using Natural Language Processing (NLP). This tool is designed to provide quick "TL;DR" snapshots of long-form web content.

## 🚀 Features

* **Automated Extraction:** Pulls main article text while ignoring ads, sidebars, and navigation menus.
* **Extractive Summarization:** Implements the **Luhn Algorithm** via the Sumy library to identify and rank the most significant sentences.
* **Flexible Output:** Customize the summary length dynamically through API query parameters.
* **Interactive Documentation:** Built-in Swagger UI for testing endpoints in real-time.

## 🛠️ Tech Stack

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **NLP Engine:** [Sumy](https://github.com/miso-belica/sumy) & [NLTK](https://www.nltk.org/)
* **Web Scraping:** [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)
* **Server:** [Uvicorn](https://www.uvicorn.org/)

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone [https://github.com/yourusername/article-summarizer.git](https://github.com/yourusername/article-summarizer.git)
cd article-summarizer
```

### 2. Install Dependencies
```bash
pip install fastapi uvicorn beautifulsoup4 requests sumy nltk
```

### 3. Initialize NLP Resources
The first time you run the project, NLTK needs to download the `punkt_tab` tokenizer. The application handles this automatically via the `lifespan` event, but you can also run:
```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

### 4. Run the API
```bash
uvicorn main:app --reload
```
View the interactive documentation at `http://127.0.0.1:8000/docs`.

## 📖 Usage Example

**Endpoint:** `POST /summarize`

**Parameters:**
* `url`: The full link to the article.
* `count`: (Optional) The number of sentences to return (Default: 3).

**Sample Request:**
```bash
curl -X 'POST' \\
  '[http://127.0.0.1:8000/summarize?url=https://example.com/news-article&count=3](http://127.0.0.1:8000/summarize?url=https://example.com/news-article&count=3)' \\
  -H 'accept: application/json'
```

**Sample Response:**
```json
{
  "url": "[https://example.com/news-article](https://example.com/news-article)",
  "summary": [
    "The primary discovery indicates a shift in global trends.",
    "Researchers noted that the secondary effects were more significant than expected.",
    "The study concludes that immediate action is required to balance the system."
  ]
}
```

---

## ⚠️ Demerits & Technical Limitations

As an open-source project, it is important to acknowledge the inherent limitations of the current logic:

### 1. Extractive vs. Abstractive Summarization
Unlike LLMs (like GPT-4), this tool uses **Extractive** logic. It identifies the "best" existing sentences and copies them. It does not rewrite or paraphrase text, which can sometimes lead to a "choppy" reading experience if sentences rely heavily on previous context.

### 2. The "Bot Block" & Paywall Issue
The scraper uses the `requests` library. Many high-authority sites (New York Times, Medium, etc.) detect automated scripts and will return a `403 Forbidden` error or block the content. Advanced headers or proxy rotation would be required to bypass this.

### 3. JavaScript-Heavy Sites (SPA)
This tool parses raw HTML. If a website loads its content dynamically using JavaScript (React, Vue, etc.), the scraper will see an empty page, resulting in an empty summary.

### 4. Logic Bias (Luhn Algorithm)
The Luhn algorithm calculates importance based on word frequency. If an article repeats certain buzzwords frequently in non-essential sections (like a disclaimer or a repetitive intro), the algorithm may incorrectly prioritize those sentences.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the scraping logic or implement **Abstractive** summarization, please feel free to open an issue or submit a Pull Request.
