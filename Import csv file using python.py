import pandas as pd

try:
    df = pd.read_csv(r'C:\Users\ELCOT\Documents\SSMS\Project 1-Sheet1.csv')
    print("File loaded successfully!")
    print(df.head())
except FileNotFoundError:
    print("File not found. Check the file path.")
except Exception as e:
    print("Error:", e)
