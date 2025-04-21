from scraper import scrape_page
from analyzer import analyze_sentiment

def main():
    try:
        with open("urls.txt", "r") as file:
            urls = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("urls.txt not found.")
        return

    for url in urls:
        print(f"\nScraping: {url}")
        content = scrape_page(url)
        sentiment = analyze_sentiment(content)
        print(sentiment)

if __name__ == "__main__":
    main()