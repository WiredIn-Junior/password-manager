# Password Manager Application V1 By Dev WiredIn-Junior
# Import Needed Libs
import os
import time
import password_manager as pm
import utils as us
# import colorama
# Main Code Block
print("Welcome To Password ManagerV2 By Dev WiredIn-Junior")
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
        finalpassword = ""
        pw_gen_ask = input("Would You Like To Generate Strong Password(Y/n, default = N)").lower()
        if pw_gen_ask == "y":
            passlength = input("Enter Password Length(Default 8): ")
            if passlength == "":
                passlength = 8
            else:
                None
            generatedpassword = us.password_generator(passlength)
            print(f"Generated Password: {generatedpassword}")
            generatedpassword = finalpassword
        else:
            pw = input("Please Enter The Password: ")
            pw = finalpassword
        notes = input("Enter Note: ")
        pm.addpassword(site, user, finalpassword, notes)
        time.sleep(1)
        us.clearscreen()
    elif choice == "2":
        us.clearscreen()
        pm.viewpassword()
    elif choice == "3":
        pm.searchpassword()
    elif choice == "4":
        pm.deletepassword()
        time.sleep(2)
        us.clearscreen()
    elif choice == "5":
        print("See You Soon..")
        time.sleep(3)
        os._exit()