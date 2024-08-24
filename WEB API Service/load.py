import pandas as pd
import sqlite3

# Load the data from the CSV file
csv_file = 'zomato.csv'
df = pd.read_csv(csv_file, encoding='ISO-8859-1')

# Connect to SQLite database
conn = sqlite3.connect('zomato.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    Restaurant_ID INTEGER PRIMARY KEY,
    Restaurant_Name TEXT,
    Country_Code INTEGER,
    City TEXT,
    Address TEXT,
    Locality TEXT,
    Locality_Verbose TEXT,
    Longitude REAL,
    Latitude REAL,
    Cuisines TEXT,
    Average_Cost_for_two INTEGER,
    Currency TEXT,
    Has_Table_booking TEXT,
    Has_Online_delivery TEXT,
    Is_delivering_now TEXT,
    Switch_to_order_menu TEXT,
    Price_range INTEGER,
    Aggregate_rating REAL,
    Rating_color TEXT,
    Rating_text TEXT,
    Votes INTEGER
)
''')

# Insert data into the table
df.to_sql('restaurants', conn, if_exists='replace', index=False)

# Commit and close the connection
conn.commit()
conn.close()

print("Data loaded successfully!")
