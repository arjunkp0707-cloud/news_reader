# 📰 News Fetcher using Python (NewsAPI)

A simple Python script that fetches the latest news articles based on user input using the **NewsAPI** service.

---

## 🚀 Features

- 🔍 Search news by keyword/topic
- 🕒 Fetch latest articles sorted by publish date
- 🌐 Direct links to full news articles
- 📄 Clean and readable console output

---

## 🛠️ Tech Stack

- **Python 3**
- **Requests Library**
- **NewsAPI**

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/news-fetcher.git
cd news-fetcher
```

2. Install required package:

```bash
pip install requests
```

---

## 🔑 Setup API Key

1. Go to: https://newsapi.org/
2. Sign up and get your API key
3. Replace this line in your code:

```python
api = "YOUR_API_KEY_HERE"
```

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then enter a topic when prompted:

```
what type of news are you interested today? technology
```

---

## 📌 Example Output

```
1 Apple announces new AI chip https://example.com/article1

****************************************

2 Latest AI breakthrough in 2026 https://example.com/article2

****************************************
```

---

## ⚠️ Important Notes

- Free NewsAPI accounts have **date range limits**.
  If you get an error like:

  ```
  "You are trying to request results too far in the past"
  ```

  👉 Use a recent date (last 30 days), for example:

```python
from=2026-06-20
```

- API has request limits (e.g., 100 requests/day for free plan)

---

## 🧠 Improvements You Can Add

- Save news to a **CSV or JSON file**
- Add **category-based filtering** (sports, business, etc.)
- Build a **GUI app using Tkinter**
- Convert into a **FastAPI backend project**

---

## 📂 Project Structure

```
news-fetcher/
│── main.py
│── README.md
```

---

## 👨‍💻 Author

**Arjun K P**

---

## 📜 License

This project is open-source and free to use.
