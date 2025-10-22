import requests;
from bs4 import BeautifulSoup
import pandas as pd
import time
 
# Step 1: Fetch the website
url = "https://quotes.toscrape.com"
headers = {"User-Agent": "Mozilla/5.0"}  # respectful request headers
 
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # handle bad status codes
    time.sleep(2)  # delay between requestsṇṇ
except requests.exceptions.RequestException as e:
    print("❌ Error fetching the website:", e)
    exit()
 
# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")
 
# Step 3: Extract data
quotes_data = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    tags = [tag.get_text() for tag in quote.find_all("a", class_="tag")]
    
    quotes_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })
 
# Step 4: Store in CSV
df = pd.DataFrame(quotes_data)
df.to_csv("quotes_raw.csv", index=False)
print("✅ Raw data saved as 'quotes_raw.csv'")