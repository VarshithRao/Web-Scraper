Web Scraper

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

***Requirements***

*   Python 3.7+                        
*   requests
*   beautifulsoup4

INSTALL DEPENDENCES USING :
pip install requests beautifulsoup4


***License***
MIT License – Free to use, modify, and distribute