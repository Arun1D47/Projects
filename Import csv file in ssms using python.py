import pandas as pd
import pyodbc

# Read CSV File
df = pd.read_csv(
    r'C:\Users\ELCOT\Documents\SSMS\Project 1-Sheet1.csv'
)

# Convert BillDate column to date format
df['BillDate'] = pd.to_datetime(df['BillDate'])

# SQL Server Connection
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=PRADEEP\\SQLEXPRESS;'
    'DATABASE=retail_sales_details;'
    'Trusted_Connection=yes;'
)

cursor = conn.cursor()

# Insert Query
query = """
INSERT INTO SalesData
(BillID, BillDate, CustomerName, City,
 ProductName, PaymentMethod, Quantity, Amount)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

# Insert Data
for _, row in df.iterrows():
    cursor.execute(
        query,
        int(row['BillID']),
        row['BillDate'],
        row['CustomerName'],
        row['City'],
        row['ProductName'],
        row['PaymentMethod'],
        int(row['Quantity']),
        float(row['Amount'])
    )

# Save Changes
conn.commit()

print("CSV data loaded successfully into SalesData table.")

# Close Connection
cursor.close()
conn.close()
