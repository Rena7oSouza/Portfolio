# 🕸️ WebScrapper USD-BRL Exchange Rate

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pytest](https://img.shields.io/badge/Tested%20with-Pytest-green)
![Behave](https://img.shields.io/badge/Tested%20with-Behave-orange)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A **simple webscraper project** developed in Python, using **MVC architecture**, to scrape the current USD-BRL exchange rate from Google and save it to a CSV file. Includes a **Tkinter GUI**, unit tests with **Pytest**, and BDD tests with **Behave**.

---

## 🚀 **Features**

✅ MVC Project Structure  
✅ Tkinter GUI for user interaction  
✅ Web scraping with Requests + BeautifulSoup  
✅ Save results to CSV using Pandas  
✅ Unit Tests with Pytest  
✅ BDD Tests with Behave

---

## 🗂️ **Project Structure**

WebScrapper/
├── app/
│ ├── controller/
│ │ └── scraper_controller.py
│ ├── model/
│ │ └── exchange_model.py
│ ├── view/
│ │ ├── exchange_view.py
│ │ └── exchange_gui.py
│ └── init.py
├── tests/
│ ├── test_scraper.py
│ └── features/
│ ├── exchange.feature
│ └── steps/
│ └── steps_exchange.py
├── main.py
├── requirements.txt
└── README.md


---

## 💻 **How to Run**

### 🔧 **1. Clone the repository**

```bash
git clone https://github.com/yourusername/WebScrapper.git
cd WebScrapper
```

### 🔧 2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

### 🔧 3. Install dependencies

pip install -r requirements.txt

⚠️ Linux only

Install Tkinter if not installed:

sudo apt install python3-tk

### 🔧 4. Run the GUI

python3 main.py

### 🔧 5. Run unit tests

PYTHONPATH=$(pwd) pytest tests/

### 🔧 6. Run BDD tests

PYTHONPATH=$(pwd) behave tests/features/

## 📝 Requirements

    Python 3.12+

    requests

    beautifulsoup4

    pandas

    pytest

    behave

    tk (system package on Linux)


✨ Author

Renato Souza
GitHub Profile


💡 Future improvements

    Docker containerization

    Schedule scraping with APScheduler or cron

    Integration with a database (SQLite or PostgreSQL)

    Export data visualization with Matplotlib

