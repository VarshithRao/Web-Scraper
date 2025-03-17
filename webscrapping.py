import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get information from a Wikipedia page
def scrape_wikipedia_info(url):
    # Send the GET request to the Wikipedia page
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title of the Wikipedia page
        title = soup.find('h1', {'id': 'firstHeading'}).text
        print(f"Title of the Page: {title}\n")
        
        # Extract the first paragraph (introduction) of the page
        intro_paragraph = soup.find('div', {'class': 'reflist'}).find_previous('p').text.strip()
        print(f"Introduction: \n{intro_paragraph}\n")
        
        # Extract all links on the page
        print(f"Links on this page (first 5 links):")
        links = soup.find_all('a', href=True)
        for link in links[:5]:  # Show the first 5 links
            print(link['href'])
        
        # Extract images on the page
        print(f"\nImages on this page (first 3 images):")
        images = soup.find_all('img', src=True)
        for img in images[:3]:  # Show the first 3 images
            print("https:" + img['src'])  # Full URL of the image
            
        # Extract table of contents (if present)
        print("\nTable of Contents:")
        toc = soup.find('div', {'id': 'toc'})
        if toc:
            toc_items = toc.find_all('span', {'class': 'toctext'})
            for item in toc_items:
                print(item.text)
        
        # Extract the infobox (if present, as a table)
        print("\nInfobox (if present):")
        infobox = soup.find('table', {'class': 'infobox'})
        if infobox:
            rows = infobox.find_all('tr')
            for row in rows:
                th = row.find('th')
                td = row.find('td')
                if th and td:
                    print(f"{th.text.strip()}: {td.text.strip()}")
        
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# URL of the Wikipedia page to scrape
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# Call the function to scrape the Wikipedia page
scrape_wikipedia_info(url)
