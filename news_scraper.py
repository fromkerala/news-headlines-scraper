print(">>> Script started")

import requests
from bs4 import BeautifulSoup

print(">>> Libraries imported")

url = 'https://news.ycombinator.com/'

headers = {'User-Agent': 'Mozilla/5.0'}

try:
    print("[+] Sending GET request...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    print("[+] Parsing HTML...")
    soup = BeautifulSoup(response.text, 'html.parser')

    print("[+] Finding headlines...")
    headlines = soup.find_all('h2')

    print(f"[+] Found {len(headlines)} <h2> tags.")
    
    titles = [h.text.strip() for h in headlines if h.text.strip()]
    
    with open('headlines.txt', 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')

    print(f"[✓] Saved {len(titles)} headlines to headlines.txt")

except Exception as e:
    print("[-] Error occurred:", e)
