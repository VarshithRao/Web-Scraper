Web Scraper
Overview

This is a robust and flexible web scraper built using Python, requests, and BeautifulSoup. It is designed to extract essential information from any website, such as the page title, first paragraph, links, and images. The scraper is built to handle common web scraping challenges like access restrictions, SSL certificate issues, and temporary network errors.

Features

Generic scraping: Works on any website, not limited to Wikipedia.

Title extraction: Captures the <title> of the web page.

Introduction paragraph: Extracts the first meaningful paragraph <p> for a quick summary.

Links extraction: Collects all links (<a href>) and displays the first few.

Image extraction: Finds all <img> sources and displays the first few, handling relative URLs.

Retry mechanism: Automatically retries requests in case of temporary failures or HTTP errors like 403 Forbidden.

Delay between requests: Randomized delays to reduce the risk of being blocked by websites.

SSL error handling: Automatically retries with SSL verification disabled if a certificate error occurs.

Exception handling: Gracefully handles network errors, HTTP errors, and parsing errors without crashing.

Requirements

Python 3.7+

requests

beautifulsoup4

Install dependencies using:

pip install requests beautifulsoup4

Usage
from scraper import scrape_generic_website

<!-- url = "https://spring.io/projects/spring-boot" -->
scrape_generic_website(url)


The script prints:

The page title

The first paragraph

The first 5 links

The first 3 images

Optional Settings

Retries: Customize the number of retries if the request fails.

Delay: Adjust minimum and maximum delay between requests.

SSL Verification: Enable or disable SSL certificate verification.

Example:

scrape_generic_website(url, retries=5, delay_range=(2, 5), verify_ssl=True)

Notes

Designed for educational and personal use.

Avoid sending too many requests too quickly to prevent blocking by websites.

Some websites may have dynamic content (JavaScript-loaded) which this scraper cannot handle directly.

License

MIT License – Free to use, modify, and distribute.