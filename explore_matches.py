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

# Step 4: Query the database and explore matches
print("Exploring matches...")

# Example Query: Fetch the first 5 rows from the 'Match' table
query = "SELECT * FROM Match LIMIT 5;"
matches = pd.read_sql_query(query, conn)

# Display the fetched data
print(matches)

# Example Query: Count the number of matches in the dataset
query_count = "SELECT COUNT(*) as total_matches FROM Match;"
total_matches = pd.read_sql_query(query_count, conn)
print(f"Total number of matches in the dataset: {total_matches['total_matches'].iloc[0]}")

# Step 5: Close the database connection
conn.close()
print("Database connection closed.")
