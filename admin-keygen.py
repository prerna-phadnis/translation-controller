# admin_keygen.py
import sys
from cryptography.fernet import Fernet

# 1. This is your MASTER KEY. 
# You must paste this EXACT key into your run_app.py variable 'SECRET_KEY'
# Generate a new one once by running: Fernet.generate_key()
SECRET_KEY = b'2avw6AEzFpQO-Zt-a0gxSndOcwRJC5QobzJzijHFW1o=' 

def generate_license(user_hwid):
    cipher_suite = Fernet(SECRET_KEY)
    
    # We encrypt the user's HWID. 
    # This creates a token that only WE could have created (because we have the Key).
    encrypted_token = cipher_suite.encrypt(user_hwid.encode())
    
    filename = f"Chinese_PDF_Translation_license.dat"
    with open(filename, "wb") as f:
        f.write(encrypted_token)
    
    print(f"\n✅ Success! License saved to: {filename}")
    print(f"Content: {encrypted_token.decode()}\n")

if __name__ == "__main__":
    print("--- OFFINE LICENSE GENERATOR ---")
    hwid = input("Enter Customer's HWID: ").strip()
    generate_license(hwid)