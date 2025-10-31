import requests
from bs4 import BeautifulSoup
import time
import random
from requests.exceptions import RequestException, SSLError

def scrape_generic_website(url, retries=3, delay_range=(1, 3), verify_ssl=True):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36"
    }

    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url, headers=headers, verify=verify_ssl)
            
            if response.status_code == 403:
                print("403 Forbidden: Access denied. Retrying after a delay...")
                time.sleep(random.uniform(*delay_range))
                attempt += 1
                continue
            elif response.status_code == 404:
                print("404 Not Found: The page does not exist.")
                return
            elif response.status_code != 200:
                print(f"Failed to retrieve page. Status code: {response.status_code}")
                return

            # Parse the page
            soup = BeautifulSoup(response.text, 'html.parser')

            # Title
            title = soup.title.text.strip() if soup.title else "No title found"
            print(f"Title: {title}\n")

            # First paragraph
            paragraphs = soup.find_all('p')
            intro_paragraph = paragraphs[0].text.strip() if paragraphs else "No paragraph found"
            print(f"First paragraph:\n{intro_paragraph}\n")

            # Links (all)
            links = [link['href'] for link in soup.find_all('a', href=True)]
            print(f"First 5 links:")
            for link in links[:5]:
                print(link)

            # Images
            images = [img['src'] for img in soup.find_all('img', src=True)]
            print(f"\nFirst 3 images:")
            for img in images[:3]:
                if img.startswith("//"):
                    img = "https:" + img
                print(img)

            # Random delay before finishing
            time.sleep(random.uniform(*delay_range))
            break  # Exit retry loop after success

        except SSLError as ssl_err:
            print(f"SSL error: {ssl_err}")
            if not verify_ssl:
                print("Already ignoring SSL errors, cannot proceed.")
                return
            print("Retrying with SSL verification disabled...")
            verify_ssl = False
            attempt += 1
        except RequestException as e:
            print(f"Request error: {e}. Retrying...")
            time.sleep(random.uniform(*delay_range))
            attempt += 1

# Example usage
url = "https://www.tutorialspoint.com/jenkins/index.htm"
scrape_generic_website(url)
