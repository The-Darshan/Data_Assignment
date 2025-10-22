
from cryptography.fernet import Fernet
 
# Step 1: Generate a key and save it (do this once)
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)
 
# Step 2: Use the key to encrypt data
with open("quotes_raw.csv", "rb") as file:
    original_data = file.read()
 
fernet = Fernet(key)
encrypted_data = fernet.encrypt(original_data)
 
# Step 3: Save encrypted file
with open("quotes_encrypted.csv", "wb") as enc_file:
    enc_file.write(encrypted_data)
 
print("🔐 Data encrypted and saved as 'quotes_encrypted.csv'")
 
# Optional: Decrypt later
with open("secret.key", "rb") as key_file:
    key = key_file.read()
fernet = Fernet(key)
decrypted_data = fernet.decrypt(encrypted_data)
with open("quotes_decrypted.csv", "wb") as dec_file:
    dec_file.write(decrypted_data)
 
print("✅ Data decrypted and saved as 'quotes_decrypted.csv'")