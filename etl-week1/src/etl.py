import os
import time
import pandas as pd
import psycopg2
from validation import DataRow


def main():
    # Load CSV
    df = pd.read_csv('/app/data/sample.csv')

    retries = 10
    for i in range(retries):
        try:
            conn = psycopg2.connect(
                host=os.getenv("POSTGRES_HOST"),
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                port=os.getenv("POSTGRES_PORT")
            )
            print("Connected to Postgres!")
            break
        except psycopg2.OperationalError as e:
            print(f"Connection failed (attempt {i + 1}/{retries}), retrying...")
            time.sleep(3)
    cur = conn.cursor()

# Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INT PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    """)

# Insert data
for _, row in df.iterrows():
    try:
        validated = DataRow(**row)
        cur.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
                (validated.id, validated.name, validated.email))
        #cur.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING",
        #        (row['id'], row['name'], row['email']))
    except:
        pass

conn.commit()
cur.close()
conn.close()
