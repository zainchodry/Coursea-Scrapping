# Coursera Python Courses Scraper

## 📌 Overview
This project is a professional-grade web scraper that extracts **Python course details** from [Coursera](https://www.coursera.org/) search results using **Python, Selenium, and BeautifulSoup**.

The scraper collects:
- **Course Title**
- **Description**
- **Rating**
- **Time Period / Duration**

The scraped data is exported to **CSV** and **Excel** formats for further analysis.

---

## 📂 Project Structure

```
coursera_scraper/
│
├── coursera_scraper.py    # Main scraping script
├── coursera.csv           # Output data (CSV)
├── coursera.xlsx          # Output data (Excel)
└── README.md              # Project documentation
```

---

## 🚀 Features
- Scrapes multiple course details from Coursera search results.
- Extracts **Title**, **Description**, **Rating**, and **Duration**.
- Saves data in both **CSV** and **Excel** formats.
- Uses `Selenium` for rendering dynamic content.
- Uses `BeautifulSoup` for parsing HTML.
- Implements **headless browsing** for faster execution.

---

## 🛠️ Requirements

Install the following Python packages before running the script:

```bash
pip install requests beautifulsoup4 selenium pandas openpyxl
```

You will also need:
- **Google Chrome** browser installed
- **ChromeDriver** (matching your Chrome version) in your system PATH

---

## ▶️ Usage

1. Clone this repository or download the ZIP.
2. Open a terminal inside the project folder.
3. Run the scraper script:

```bash
python coursera_scraper.py
```

4. The results will be saved as:
   - `coursera.csv`
   - `coursera.xlsx`

---

## ⚠️ Notes
- Coursera uses dynamic IDs for some elements, so selectors are built to handle this.
- The script uses a **randomized delay** to reduce the risk of being blocked.
- This is for **educational purposes** only; scraping should respect website terms of service.

---

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.