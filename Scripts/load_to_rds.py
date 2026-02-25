import psycopg2
import csv
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Database connection parameters
DB_HOST = "process-log-db.cqxca0keuixw.us-east-1.rds.amazonaws.com"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = 5432

conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)

cursor = conn.cursor()

# connection to database
with open("structured_logs.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        raw_timestamp = row["timestamp"]

        # Changing the comman in the timestamp to dot
        cleaned_timestamp = raw_timestamp.replace(",", ".")

        parsed_timestamp = datetime.strptime(
            cleaned_timestamp,
            "%Y-%m-%d %H:%M:%S.%f"
        )

        cursor.execute(
            """
            INSERT INTO logs_table (timestamp, level, user_id, action, status)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                parsed_timestamp,   
                row["level"],
                row["user_id"],
                row["action"],
                row["status"]
            )
        )

conn.commit()
cursor.close()
conn.close()

print("Data successfully loaded into RDS.")
