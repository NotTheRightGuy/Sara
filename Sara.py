import sys
from quotes import give_me_a_random_quote
from quotes import quote_decorator
import pickle
import time
import datetime
import os
import subprocess
import shutil


with open ('user_data.txt', 'r') as file:
    data = file.read()

clear = lambda : os.system('cls')
if len(data) == 0:
    print("Before we start I would like to know you, press 'Y' if you want to continue, or 'Q' to end")
    first_response = input(">>>")
    if first_response.lower() == "y":
        print("\nLet's continue then\n")
    elif first_response.lower() == 'q':
        sys.exit()
    else:
        print("Invalid Response, Continuing anyway\n")

#----------Asking user for information for first time usage-------------------
    print("\nWhat should I call you?")
    name = input(">>>")
    name = name.title()


    print("\nWhen is your birthday {}?  #Enter in the form of dd/mm/yyyy".format(name))
    raw_bday =  input(">>>")
    raw_bday= raw_bday.split('/')
    b_day = raw_bday[0]
    b_month = raw_bday[1]
    b_year =  raw_bday[2]

    print("\nIf you are on Instagram, what is your username?   #Feel free to skip if you don't want to.")
    insta_username = input(">>>")

    clear()
    print("In order to keep your journal writing safe, you will be asked to keep a username and password\nPlease " +
          "remember this in order to access journal the next time you open me.\n ")
    journal_username = input("Enter your username:\n>>>")
    journal_password = input("Enter your password:\n>>>")
    print("username and password set. Always remember this or else we have to reset back")

    dict_to_write = {"Name":name,"Birthday Day": b_day,"Birthday Month":b_month ,"Birthday Year":b_year ,
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

#-----------------------End of requesting user Information----------------------------------------



with open('user_data.txt','rb') as file:
    user_data = pickle.load(file)

real_username = user_data['username']
real_password = user_data['password']

print("Please enter your credentials to move ahead")
username_given = input("Username: ")
password_given = input("Password: ")
if username_given == real_username and password_given == real_password:
    print("Login Successful")

    name = user_data['Name']
    age = user_data['Age']
    b_day = user_data['Birthday Day']
    b_month = user_data['Birthday Month']
    b_year = user_data['Birthday Year']

    time.sleep(2)
    clear()
    # --------------------All this to get the current time------------------------------#
    today = datetime.datetime.today()
    current_year = today.strftime("%Y")
    day_month_year = today.strftime("%d%m%Y")
    now = datetime.datetime.now()
    current_time = now.strftime("%M%H")
    current_time_use = str(current_time)
    age = int(current_year) - int(b_year)
    # -----------------------------------------------------------------------------------#
    print("So What would you like to do today? ")

    while True:
        print("Enter 1 for your Journal")
        #TODO: To Implement more features here
        #TODO: A memo to remember your friends birthday
        #TODO: A minimal google Search
        #TODO: Suggest a song
        #TODO: Link to Lofi Stream
        #TODO: Solving a problem???
        response = input(">>>")

        if response == '1':
            clear()

            quote , author = give_me_a_random_quote()
            quote_decorator(quote,author)

            print("\n")
            print("\nEnter 1 to make a journal entry")
            print("Enter 2 to read your journal entry")
            print("Enter 3 to delete all your journal entry")
            response_for_journal = input("\n>>>")
            if response_for_journal == '1':
                print("How are you feeling right now?")
                mood = input(">>>")

                os.chdir('journals')

                try:
                    os.mkdir(str(day_month_year))
                except FileExistsError:
                    pass
                os.chdir(day_month_year)
                with open(current_time_use+'.txt','w') as file:
                    to_write = "Current Mood : {}".format(mood)
                    journal_date = today.strftime("%A %d %B %Y")
                    to_write_date = "Date: {}".format(journal_date)
                    to_write_time = "Time: {}".format(today.strftime("%I:%M %p"))
                    file.write(to_write)
                    file.write("\n")
                    file.write(to_write_date)
                    file.write("\n")
                    file.write(to_write_time)
                    file.write("\n>")

                subprocess.Popen(["notepad.exe",current_time_use])
            elif response_for_journal == '3':
                print("Deleting all the journal records")
                os.chdir('journals')
                for folder in os.listdir():
                    shutil.rmtree(folder)
                time.sleep(2)

        print("Returning back to main Menu")
        time.sleep(1)
        clear()

else: #The Else command if the user fails to provide the right password
    print("Invalid Credentials, exiting now")
    time.sleep(2)
    sys.exit()
