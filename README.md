# News Headlines Scraper

## Objective
This script scrapes top news headlines from BBC News using Python, `requests`, and `BeautifulSoup`.

## How it works
- Sends an HTTP GET request to the website.
- Parses HTML and extracts all `<h2>` tags.
- Saves cleaned headlines to `headlines.txt`.

## Requirements
- requests
- beautifulsoup4

## Usage
```bash
python scraper.py
