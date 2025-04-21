import asyncio
from scraper import scrape_all_urls
from analyzer import analyze_sentiment
from database import save_to_db
import sqlite3

# Sample URLs for scraping
urls = [
    'https://example.com',
    'https://anotherexample.com',
    'https://yetanotherexample.com'
]

async def main():
    # Scrape data from URLs
    scraped_data = await scrape_all_urls(urls)
    
    # For each URL, analyze sentiment and save to database
    conn = sqlite3.connect('scraped_data.db')
    for data in scraped_data:
        sentiment = analyze_sentiment(data['text'])
        save_to_db(conn, data['url'], sentiment, data['text'])

    conn.close()

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
