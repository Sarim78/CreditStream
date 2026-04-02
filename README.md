# CreditStream
> A Python ETL pipeline that processes 50,000 real-world loan records, extracting raw CSV data, transforming it into clean structured data, and loading it into a SQLite database.

---

## 📌 What It Does

| Step | Description |
| --- | --- |
| **Extract** | Reads raw loan portfolio data from a CSV file |
| **Transform** | Cleans nulls, fixes data types, engineers new columns |
| **Load** | Stores the cleaned data into a SQLite database |
| **Summarize** | Prints a pipeline report with key stats and breakdowns |

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

* **50,000 loans** across **10 industry sectors**
* Sectors include Technology, Healthcare, Real Estate, Financials, and more
* Features include credit score, default status, loan type, risk metrics, and more

---

## ⚙️ Transform Details

The transform step performs the following:

- Drops duplicate rows
- Removes records missing critical fields (`loan_id`, `credit_score`, `ead`, `defaulted`)
- Parses `origination_date` and `maturity_date` as datetime
- Fills missing numeric values with `0`
- Strips whitespace from all string columns
- Engineers two new columns:
  - `risk_tier` — classifies each loan as `Low` / `Medium` / `High` risk based on credit score (750+ = Low, 650–749 = Medium, <650 = High)
  - `el_ratio` — calculates expected loss ratio per loan (`EL / EAD`)
  - `is_defaulted` — casts the default flag to integer (0 or 1)

---

## 🛠️ Tech Stack

* **Python** --> core language
* **pandas** --> data cleaning and transformation
* **SQLAlchemy** --> database connection and loading
* **SQLite** --> lightweight local database

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

4. View the database
   Open `output/creditstream.db` with **DB Browser for SQLite** or the
   **SQLite Viewer** extension in VS Code to inspect the loaded data.
