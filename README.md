Web Scraper
Overview

This is a robust and flexible web scraper built using Python, requests, and BeautifulSoup.
It is designed to extract essential information from any website, such as:

Page title

First paragraph

Links

Images

The scraper is built to handle common web scraping challenges like:

Access restrictions (403 Forbidden)

SSL certificate issues

Temporary network errors

Features

Generic scraping – Works on any website, not limited to Wikipedia

Title extraction – Captures the <title> of the web page

Introduction paragraph – Extracts the first meaningful <p>

Links extraction – Collects all links (<a href>) and displays the first few

Image extraction – Finds all <img> sources, handling relative URLs

Retry mechanism – Automatically retries requests in case of failures

Randomized delays – Reduces the risk of being blocked

SSL error handling – Retries with SSL verification disabled if needed

Exception handling – Handles network, HTTP, and parsing errors gracefully

Requirements

Python 3.7+

requests

beautifulsoup4

Install dependencies using:

pip install requests beautifulsoup4

Usage
from scraper import scrape_generic_website

url = "https://spring.io/projects/spring-boot"
scrape_generic_website(url)


Output includes:

Page title

First paragraph

First 5 links

First 3 images

Optional Settings

You can customize:

Retries – Number of retry attempts if request fails

Delay – Minimum and maximum delay between requests

SSL Verification – Enable or disable SSL certificate verification

Example:

scrape_generic_website(
    url, 
    retries=5, 
    delay_range=(2, 5), 
    verify_ssl=True
)

Notes

Designed for educational and personal use

Avoid sending too many requests too quickly to prevent blocking by websites

Some websites with JavaScript-loaded content may not work directly with this scraper

License

MIT License – Free to use, modify, and distribute
