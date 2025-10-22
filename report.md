📘 Web Scraping and Data Security Project
🖥️ 1. Website Scraped
We used Books to Scrape, a website designed for practicing web scraping. It was selected because:

✅ Educational and scraping-friendly

📚 Structured book data

🔄 Consistent formatting

📊 Multiple attributes per item

⚡ Reliable uptime and performance

📦 2. Data Fields Extracted
The following fields were extracted from each book listing:

Field	Description	Example
Title	Full book title	"The Great Gatsby"
Price	Price in GBP (£)	"£9.99"
Availability	Stock status	"In stock"
Rating	Star rating (One to Five)	"Four"
Data was saved in CSV format for easy analysis.

🔐 3. Security Measures
To protect the scraped data, we implemented encryption using the cryptography library.

🔑 A. Encryption Strategy
Fernet symmetric encryption

Secure key generation and storage

Support for both encryption and decryption

python
# Key Generation
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Encryption
fernet = Fernet(key)
encrypted_data = fernet.encrypt(original_data)
🔄 B. Data Protection Workflow
Save raw data to books_raw.csv

Encrypt and store as books_encrypted.csv

Store encryption key separately in secret.key

Verify decryption via books_decrypted.csv

⚙️ 4. Challenges Faced
🧩 Technical Challenges
HTML Navigation: Solved using BeautifulSoup with class selectors and error handling

Data Integrity: Verified through decryption testing

File Handling: Managed with context managers (with statements)

🔧 Implementation Challenges
Key Management: Resolved by separating key storage

Error Handling: Used try-except blocks for network resilience

🧪 5. Code Snippets
🕸️ Web Scraping
python
# Extract book data
for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    availability = book.find("p", class_="instock").text.strip()
    rating = book.find("p", class_="star-rating")["class"][1]
🔐 Data Encryption
python
# Encrypt raw CSV data
with open("books_raw.csv", "rb") as file:
    original_data = file.read()

fernet = Fernet(key)
encrypted_data = fernet.encrypt(original_data)

with open("books_encrypted.csv", "wb") as enc_file:
    enc_file.write(encrypted_data)
🧭 6. Ethical Considerations
✅ Responsible Practices
Rate Limiting: Added 2-second delay between requests

python
time.sleep(2)
User-Agent Identification:

python
headers = {"User-Agent": "Mozilla/5.0"}
Data Protection: Encrypted sensitive data and securely managed keys