# Password Manager Application V1 By Dev WiredIn-Junior
# Import Needed Libs
import os
import time
# import colorama
# Adding Passwords Function
def addpassword(website, username, password, notes):
    pass_data = f"Website: {website}\nUsername: {username}\nPassword: {password}\nNote: {notes}\n------------\n"
    with open("passwords.txt", "a") as p:
        p.write(pass_data)
    print("Password Added Successfully")
# Viewing Passwords Function
def viewpassword():
    try:
        with open("passwords.txt", "r") as p:
            print(f"Your Passwords:\n{p.read()}")
    except FileNotFoundError:
        print("File Not Found")
    except:
        print("Something Went Wrong!")
# Searching Function
def searchpassword():
    print("Enter Website Name")
    website = input("Website: ")
    print("------------")
    with open("passwords.txt", "r") as file:
        entries = file.read().split("------------")
    
    found = False
    for entry in entries:
        if f"Website: {website}" in entry:
            print(entry)
            found = True
    
    if not found:
        print("Not Found")
# Deleting Passwords Function
def deletepassword():
    print("Enter Website Name")
    website = input("Website: ")
    print("------------")
    with open("passwords.txt", "r") as file:
        entries = file.read().split("------------")
    
    with open("passwords.txt", "w") as file:
        for entry in entries:
            if f"Website: {website}" not in entry:
                file.write(entry + "------------")
    print("Deleted Successfully")
# Main Code Block
print("Welcome To Password ManagerV1 By Dev WiredIn-Junior")
while True:
    print("==== Password Manager ====")
    print("1.Add Password")
    print("2.View Passwords")
    print("3.Search Password")
    print("4.Delete Password")
    print("5.Exit")
    choice = input("Enter Your Choice: ")
    if choice == "":
        print("Choice Can't Be Empty")
        continue
    elif choice == "1":
        print("Please Enter Your Credentials")
        while True:
            site = input("Please Enter Website: ").strip().lower()
            if site == "":
                print("Site Cannot Be Empty")
                continue
            break
        user = input("Please Enter Username: ")
        pw = input("Please Enter The Password: ")
        notes = input("Enter Note: ")
        addpassword(site, user, pw, notes)
    elif choice == "2":
        viewpassword()
    elif choice == "3":
        searchpassword()
    elif choice == "4":
        deletepassword()
    elif choice == "5":
        print("See You Soon..")
        time.sleep(3)
        os._exit()