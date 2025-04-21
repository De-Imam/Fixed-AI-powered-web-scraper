import aiohttp
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# Function to handle JavaScript-rendered websites using Selenium
def scrape_dynamic_content(url):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='/path/to/chromedriver', options=options)
    driver.get(url)
    time.sleep(5)  # Wait for content to load
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')
    return ' '.join([p.get_text() for p in paragraphs])

# Asynchronous scraping with aiohttp
async def scrape_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                paragraphs = soup.find_all('p')
                text = ' '.join([p.get_text() for p in paragraphs])
                return {'url': url, 'text': text}
            return {'url': url, 'text': ''}

# Asynchronous entry point to scrape multiple URLs
async def scrape_all_urls(urls):
    tasks = [scrape_url(url) for url in urls]
    results = await asyncio.gather(*tasks)

    # For websites that need JavaScript rendering, we scrape them using Selenium
    for result in results:
        if not result['text']:  # If the text is empty, try scraping with Selenium
            result['text'] = scrape_dynamic_content(result['url'])
    
    return results
