import sqlite3
import pandas as pd

conn = sqlite3.connect("E:/GUVI/Video Game Analysis/videogames.db")
df = pd.read_sql_query("SELECT * FROM game_sales LIMIT 5;", conn)
print(df)
conn.close()
