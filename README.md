# 🎮 Video Game Sales & Engagement Analysis 🎮 



### 📌 Project Overview

This project analyzes video game sales performance and player engagement using cleaned datasets from multiple sources.
The workflow involves:

           1. Cleaning raw CSV files.
           2. Storing them in a SQLite database.
           3. Querying and visualizing the data in Power BI to generate interactive dashboards.

           

### 📂 Project Structure 📂 

    📁 Video Game Analysis
     │
     ├── games_cleaned.csv             # Cleaned engagement dataset
     ├── vgsales_cleaned.csv           # Cleaned sales dataset
     ├── create_database.py            # Script to load CSVs into SQLite DB
     ├── test_database.py              # Script to test DB connectivity
     ├── videogames.db                 # SQLite database file
     ├── PowerBI_Dashboard.pbix        # Power BI dashboard file
     └── README.md                     # Project documentation

     
     
### 🛠 Tools & Technologies 🛠

           1. Python (pandas, sqlite3)
           2. SQLite (local database)
           3. Power BI (visualization & dashboard creation)
           4. CSV Data (cleaned game engagement and sales datasets)

           

### 📊 Dataset Description

    1. game_engagement.csv
            |
            ├── Title – Game name
            ├── Plays – Total number of times played
            ├── Wishlist – Number of players who wishlisted the game
            ├── Backlogs – Players who own the game but haven’t played it yet
            ├── Ratings – Average player rating
            ├── Genres – Game categories

    2. game_sale
            |
            ├── Title – Game name
            ├── Platform – Gaming platform (e.g., PS2, Xbox, PC)
            ├── Publisher – Game publisher
            ├── Year – Release year
            ├── Global_Sales – Total worldwide sales (in millions)
            ├── Regional Sales – Sales breakdown by NA, EU, JP, and others



### 📈 Dashboard Insights 📈 

The Power BI dashboard answers questions like:

           1. Which games have the highest number of plays and wishlists?
           2. What are the top-selling games by global and regional sales?
           3. How do sales vary by genre, publisher, and year?
           4. Which platforms have dominated the market over time?
           5. Correlation between ratings and engagement.

           

### 👨‍💻 Author 👨‍💻

Nivethika G  (nive8393@gmail.com)






           
