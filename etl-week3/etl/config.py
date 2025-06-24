from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES = {
    "host": os.getenv("POSTGRES_HOST"),
    "dbname": os.getenv("POSTGRES_DB"),
    "user": os.getenv("POSTGRES_USER"),
    "password": os.getenv("POSTGRES_PASSWORD"),
    "port": os.getenv("POSTGRES_PORT")
}

CSV_PATH = os.getenv("CSV_PATH")