import sqlite3

# Create the database and table (if not already created)
def create_db():
    conn = sqlite3.connect('scraped_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sentiment_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            sentiment TEXT,
            text TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Insert data into the database
def save_to_db(conn, url, sentiment, text):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sentiment_data (url, sentiment, text)
        VALUES (?, ?, ?)
    ''', (url, sentiment, text))
    conn.commit()

# Initialize the database
create_db()
