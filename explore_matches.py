import kagglehub
import sqlite3
import os
import pandas as pd

# Step 1: Download the dataset
print("Downloading dataset...")
path = kagglehub.dataset_download("hugomathien/soccer")

# Step 2: Construct the path to the SQLite database
db_file = os.path.join(path, "database.sqlite")

# Step 3: Connect to the SQLite database
try:
    conn = sqlite3.connect(db_file)
    print("Successfully connected to the database.")
except sqlite3.OperationalError as e:
    print(f"Error: {e}")
    exit()

tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = conn.execute(tables_query).fetchall()

# Print the table names
print("Tables in the Database:")
for table in tables:
    print(table[0])

    # For each table, get the column names
    columns_query = f"PRAGMA table_info({table[0]});"
    columns_info = conn.execute(columns_query).fetchall()
    column_names = [info[1] for info in columns_info]

    print(f"Column Names in the {table[0]} Table:")
    print(column_names)
conn.close()
print("Database connection closed.")
