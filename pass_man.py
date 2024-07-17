import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

'''
# Function to load the encryption key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()
'''

# Function to derive a key from the master password
def derive_key(master_pwd, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))

# Get the master password and create the Fernet object
master_pwd = input("What is the master password: ")
salt = load_key()  # Assuming the salt is stored in the key file
key = derive_key(master_pwd, salt)
fer = Fernet(key)

# Function to view stored passwords
def view():
    with open("password_manager.txt", "r") as f:
        for line in f:
            user, passw = line.strip().split("|")
            print(f"User: {user}, Password: {fer.decrypt(passw.encode()).decode()}")

# Function to add a new password entry
def add():
    name = input("Enter the name of the entry: ")
    pwd = input("Enter the password for the entry: ")
    with open("password_manager.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")

# Main loop to handle user input
while True:
    mode = input("Would you like to add a new entry or retrieve an existing entry (view, add), press q to quit?: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
