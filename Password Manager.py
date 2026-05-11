import json
import random
import string
import base64

passwords = []

#------------------Load saved data-------------------
def load_data():
    global passwords
    try:
        with open("paswords.json","r") as file:
            passwords = json.load(file) 
    except FileNotFoundError:
        passwords = []

#------------------Save data-------------------
def save_data():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file, indent=4)
# ------------------Encryption-------------------
def encrypt_password(password):
    return base64.b64encode(password.encode()).decode()

def decrypt_password(encrypted_password):
    return base64.b64decode(encrypted_password.encode()).decode()

#------------------Password Generation-------------------
def generate_password():
    length = input("Enter password length:")
    if not length.isdigit():
        print("Invalid input! Enter numbers only.\n")
        return ""
    length = int(length)

    if length <= 0:
        print("Length must be greater than 0.\n")
        return""

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    
    for i in range(length):
        password += random.choice(characters)
    
    print("Generated password:", password)
    return password

#------------------Add account-------------------
def add_account():
    website = input("Enter website:").strip()
    if website == "":
        print("website cannot be empty.\n")
        return
    username = input("Enter username:").strip()
    if username == "":
        print("username cannot be empty.\n")
        return

    choice = input("Do you want to generate a password? (y/n):").lower()

    if choice == "y":
        password = generate_password()
    else:
        password = input("Enter password:").strip()
    if password == "":
        print("Account not saved. password is required.\n")
        return

    account = {
        "website": website,
        "username": username,
        "password": encrypt_password(password)
    } 

    passwords.append(account)
    save_data()

    print("Account saved successfully!\n")

#------------------View Accounts-------------------
def view_accounts():
    if not passwords:
        print("no accounts saved.\n")
        return
    choice = input("Do you want to view passwords? (y/n):").lower()

    print("\nSaved Accounts:")
    print("-" * 40)

    for i, acc in enumerate(passwords,start=1):
        if choice == "y":
            pwd = 
decrypt_password(acc["password"])
        else:
            pwd = "*" * len(acc["password"])

        print(f"{i}. Website:{acc['website']}, username:{acc['username']}, Password: {pwd}")
    print()

#------------------Search Account-------------------
def search_account():
    website = input("Enter website to search:").strip().lower()
    if website == "":
        print("website cannot be empty.\n")
        return
    
    for acc in passwords:
        if acc["website"].lower() == website:
            print("\nAccount found:")
            print(f"Website: {acc['website']}")
            print(f"Username: {acc['username']}")
            print(f"Password: {acc['password']}\n")
            return
        
        print("No account found.\n")  

#------------------Delete Account-------------------
def delete_account():
    website = input("Enter website to delete:").strip().lower()
    if website == "":
        print("website cannot be empty.\n")
        return

    for acc in passwords:
        if acc["website"].lower() == website:
            passwords.remove(acc)
            save_data()
            print("account deleted successfully!\n")
            return
    
    print("Account not found.\n")

#------------------Menu-------------------
def menu():
     while True:
        print("===== Password Manager =====")
        print("1.Add Acoount")
        print("2.view Account")
        print("3.Search Account")
        print("4.Delete Account")
        print("5.Exit")

        choice = input("enter your choice:")

        if choice == "1":
           add_account()
        elif choice == "2":
           view_accounts()
        elif choice == "3":
           search_account()
        elif choice == "4":
           delete_account()
        elif choice == "5":
           print("Exiting...")
           break
        else:
           print("Invalid choice\n")
                                        
#---------------------Run program----------------------
load_data()
menu()