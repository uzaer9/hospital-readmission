import os
import pandas as pd
import subprocess
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load data from SQLite
import sqlite3
conn = sqlite3.connect("database/hospital_readmission.db")
df = pd.read_sql_query("SELECT * FROM readmission_table", conn)

# Target column: convert to binary
df['readmitted_binary'] = df['readmitted'].apply(lambda x: 0 if x == 'NO' else 1)

# Drop irrelevant or non-numeric columns
drop_cols = ['encounter_id', 'patient_nbr', 'readmitted']
df = df.drop(columns=drop_cols)

# Label encode all object (categorical) columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna("Unknown")
    df[col] = LabelEncoder().fit_transform(df[col])

# Split
X = df.drop(columns=['readmitted_binary'])
y = df['readmitted_binary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
df['predicted_readmitted'] = model.predict(X)

# Save results to CSV
df.to_csv("predictions.csv", index=False)

# Print basic metrics
y_pred = model.predict(X_test)
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))
print("✅ predictions.csv saved.")
pbix_path = r"C:\Users\uzair\OneDrive\Desktop\hpm\powerbi\dashboard.pbix"

print(f"🚀 Launching Power BI file: {pbix_path}")
subprocess.Popen(["start", "", pbix_path], shell=True)