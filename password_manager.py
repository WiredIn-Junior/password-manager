# Module For Password Manager Including Functions For Adding, Viewing, Searching, Editing And Deleting Passwords
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
    print("--------------------------------------------------------------")
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
# Editing Passwords Function
def editpassword():
    pass
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