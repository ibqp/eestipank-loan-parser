# 🏦 Eestipank loan parser

A lightweight ETL tool that scrapes, parses, and processes loan statistics from [Eesti Pank](https://statistika.eestipank.ee/). Tool focuses on data related to **overdue loans** in Estonia.

Reference page: https://statistika.eestipank.ee/#/en/p/FINANTSSEKTOR/147/650

---

## 🚀 Setup

- **Prerequisites**
  - Python 3.11+
- **Installation**
  - Clone the repository
  - Create a virtual environment
  - Activate the virtual environment
  - Install dependencies: `pip install -r requirements.txt`

---

## ▶️ Run

Run the parser using: `python main.py`

The program will prompt you to enter the number of years. Then, it will fetch data on overdue loans from Eesti Pank, process it, and display an interactive chart showing the trend of overdue loans over the specified period.
