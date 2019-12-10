"""
DATA 200 Fall 2019 Homework 1
Courtney Nguyen
14SEP19
hw1-4.py

"""

## 4) Extract Usernames from Domains 

def extract_usernames_domains(emails):
    print("This function is to print out usernames from emails")
    for username in emails:
        save = username.split("@")[0]
        print (save)

emails = ["apple@gmail.com","orange@yahoo.com", "grape@abc.net", 
          "peach@fuzz.com"]
usernames = extract_usernames_domains(emails)