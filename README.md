# 🏥 Hospital Readmission Analysis & Prediction

This project analyzes hospital patient data to identify trends in readmission rates using Python, SQL, Machine Learning, and Power BI.

---

## 📂 Project Structure
hpm/
├── data/
│ └── diabetic_data.csv
├── database/
│ └── hospital_readmission.db
├── notebooks/
│ └── EDA.ipynb
├── powerbi/
│ └── readmission_dashboard.pbix
├── scripts/
│ ├── load_data.py
│ └── train_predict.py
├── requirements.txt
Tech Stack
Python: pandas, sklearn, SQLAlchemy
SQL: SQLite database for storing and querying readmission records
Power BI: Interactive dashboard for visualizing readmission patterns
ML Model: Predicting readmission using logistic regression/classifiers
---
Power BI Dashboard
Visualizes:
- % of patients readmitted
- Trends over time
- Key risk factors
- Model predictions vs actuals
---
How to Run

bash
 1. Load CSV to DB
python scripts/load_data.py

 2. Train model and generate predictions
python scripts/train_predict.py
