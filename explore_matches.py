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

# Query to get column names of the Match table
query = "PRAGMA table_info(Match);"
columns_info = conn.execute(query).fetchall()

# Extract and print column names
column_names = [info[1] for info in columns_info]
print("Column Names in the Match Table:")
print(column_names)
conn.close()
print("Database connection closed.")
