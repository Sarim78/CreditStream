# CreditStream

> A Python ETL pipeline that processes 50,000 real-world loan records, extracting raw CSV data, transforming it into clean structured data, and loading it into a SQLite database.

---

## 📌 What It Does

| Step | Description |
|------|-------------|
| **Extract** | Reads raw loan portfolio data from a CSV file |
| **Transform** | Cleans nulls, fixes data types, engineers new columns |
| **Load** | Stores the cleaned data into a SQLite database |

---

## 📂 Project Structure
```
CreditStream/
├── data/               # Raw CSV input
├── output/             # SQLite database output
├── pipeline.py         # Main ETL script
├── requirements.txt    # Project dependencies
└── README.md           
```

---

## 🗂️ Dataset

- **50,000 loans** across **10 industry sectors**
- Sectors include Technology, Healthcare, Real Estate, Financials, and more
- Features include credit score, default status, loan type, risk metrics, and more

---

## 🛠️ Tech Stack

- **Python** --> core language
- **pandas** --> data cleaning and transformation
- **SQLAlchemy** --> database connection and loading
- **SQLite** --> lightweight local database

---

## 🚀 How To Run

1. Clone the repo
```
   git clone https://github.com/Sarim78/CreditStream.git
```
2. Install dependencies
```
   pip install -r requirements.txt
```
3. Run the pipeline
```
   python pipeline.py
```

---
