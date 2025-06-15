print("🚀 Starting script...")

import pandas as pd
from sqlalchemy import create_engine
import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_path = os.path.join(base_path, "data", "diabetic_data.csv")
db_path = os.path.join(base_path, "database", "hospital_readmission.db")

print(f"📄 Loading CSV from: {csv_path}")
df = pd.read_csv(csv_path)

print(f"✅ Rows loaded: {len(df)}")

engine = create_engine(f'sqlite:///{db_path}')
df.to_sql("readmission_table", con=engine, index=False, if_exists="replace")

print(f"💾 Data saved to database at: {db_path}")
