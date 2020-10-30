import sys
import os
from quotes import give_me_a_random_quote
import pickle
import time

with open ('user_data.txt', 'r') as file:
    data = file.read()

clear = lambda : os.system('cls')
if len(data) == 0:
    print("Before we start I would like to know you, press 'Y' if you want to continue, or 'Q' to end")
    first_respone = input(">>>")
    if first_respone.lower() == "y":
        print("\nLet's continue then\n")
    elif first_respone.lower() == 'q':
        sys.exit()
    else:
        print("Invalid Response, Continuing anyway\n")

    print("\nWhat should I call you?")
    name = input(">>>")

    print("\nHow old are you {}?".format(name))
    age = input(">>>")

    print("\nWhen is your birthday {}?  #Enter in the form of dd/mm/yyyy".format(name))
    raw_bday =  input(">>>")
    raw_bday.split('/')
    b_day = raw_bday[0]
    b_month = raw_bday[1]
    b_year =  raw_bday[2]

    print("\nIf you are on Instagram, what is your username?   #Feel free to skip if you don't want to.")
    insta_username = input(">>>")

    print("In order to keep your journal writing safe, you will be asked to keep a username and password\n Please " +
          "remember this in order to access the next time you open me. ")
    journal_username = input("Enter your username\n>>>")
    journal_password = input("Enter your password\n>>>")
    print("username and password set. Always remember this or else we have to reset back")

    dict_to_write = {"Name":name,"Age":int(age),"Birthday Day": b_day,"Birthday Month":b_month ,"Birthday Year":b_year ,
                     "Instagram username": insta_username,"username":journal_username,"password":journal_password}

    with open('user_data.txt','wb') as file:
        pickle.dump(dict_to_write,file)

    clear()

    print("""
    Hi {}, I'm Sara and I will be your assistant on this journey called life. I'm not that much useful 
    at this moment and my developers are still working on me to implement more and more features everyday.
    At my current stage of working I can just be used to monitor your everyday routine and help give you
    advice to improve it.
    
    I can be used as journal and you can tell me everything you have to tell me. Think of me as your best
    friend. I might not be as special as you, but I  will be glad to be your friend.
    
    Everything you will be telling me will be saved in your local machine so no one else will be knowing 
    your secrets ;)
    
    So let's get started.
    """.format(name))

with open('user_data.txt','rb') as file:
    user_data = pickle.load(file)

name = user_data['Name'] #Fetching User Name from user_data.txt
age = user_data['Age']   #Fetching User age from user_data.txt
b_day = user_data['Birthday Day'] #------------do-----------
b_month = user_data['Birthday Month'] #--------do-----------
b_year = user_data ['Birthday Year'] #---------do-----------
username = user_data['username']
password = user_data['password']

print("Please enter your credentials to move ahead")
username_given = input("Username: ")
password_given = input("Password: ")
if username_given == username and password_given == password:
    print("Login Successful")
    time.sleep(2)
    clear()
    print("So What would you like to do today? ")

    while True:
        print("Enter 1 to write your day's experience. ")
        #TODO: To Implement more features here
        response = input(">>>")

        if response == '1':
            clear()
        quote = give_me_a_random_quote()
        print("----------------Quote of the Day---------------")
        print(quote)
        print('-----------------------------------------------')
else:
    print("Invalid Credentials, exiting now")
    time.sleep(4)
    sys.exit()