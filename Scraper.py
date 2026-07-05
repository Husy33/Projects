import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Pakistan"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Get the first paragraph
intro = soup.find("div", id="mw-content-text").find("p")
print("=== INTRO ===")
print(intro.text)

# Get infobox facts
infobox = soup.find("table", class_="infobox")
rows = infobox.find_all("tr")

print("\n=== KEY FACTS ===")
for row in rows:
    header = row.find("th")
    data = row.find("td")
    if header and data:
        print(f"{header.text.strip()} : {data.text.strip()}")