import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# BBC News URL
BBC_URL = 'https://www.bbc.com/news'

# Fetch the page
response = requests.get(BBC_URL)
soup = BeautifulSoup(response.text, 'html.parser')

# Prepare CSV file
filename = f'bbc_news_{datetime.now().strftime("%Y%m%d")}.csv'
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Headline', 'Description', 'URL'])

    # Find news articles (headlines and descriptions)
    # Use anchor tags with hrefs containing '/news/articles/'
    for a in soup.find_all('a', href=True):
        href = a['href']
        if '/news/articles/' in href:
            headline = a.get_text(strip=True)
            # Try to get description from the next sibling or parent
            description = ''
            parent = a.parent
            # Look for a <p> tag in the parent or next siblings
            if parent:
                p = parent.find('p')
                if p:
                    description = p.get_text(strip=True)
            # Compose full URL if needed
            url = href if href.startswith('http') else f'https://www.bbc.com{href}'
            if headline:
                writer.writerow([headline, description, url])

print(f"Scraped news saved to {filename}")
