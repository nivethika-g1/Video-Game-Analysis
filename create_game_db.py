import sqlite3
import pandas as pd

# Step 1: Load cleaned CSV files
games_df = pd.read_csv("games_cleaned.csv")
sales_df = pd.read_csv("vgsales_cleaned.csv")

# Step 2: Rename 'Name' column to 'Title' in sales_df for consistency
sales_df.rename(columns={"Name": "Title"}, inplace=True)

# Step 3: Connect to SQLite DB (will create if not exists)
conn = sqlite3.connect("videogames.db")

# Step 4: Write both DataFrames to the DB as tables
games_df.to_sql("game_engagement", conn, if_exists="replace", index=False)
sales_df.to_sql("game_sales", conn, if_exists="replace", index=False)

# Step 5: Optional - Create indexes for faster SQL queries
conn.execute("CREATE INDEX IF NOT EXISTS idx_title_engage ON game_engagement(Title);")
conn.execute("CREATE INDEX IF NOT EXISTS idx_title_sales ON game_sales(Title);")

# Step 6: Done
conn.commit()
conn.close()

print("✅ Database created successfully: videogames.db")
