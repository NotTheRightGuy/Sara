import sys
from quotes import give_me_a_random_quote
from quotes import quote_decorator
import pickle
import time
import datetime
import os
import subprocess
import shutil
import webbrowser
from googlesearch import search
from random_songs import give_me_random_song
from find_youtube import findYT

with open('user_data.cd', 'rb') as file:
    data = file.read()

clear = lambda : os.system('cls')
if len(data) == 0:
    with open('bdays.cd', 'wb') as file:
        di = {}
        pickle.dump(di, file)
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

    with open('user_data.cd','wb') as file:
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


with open('user_data.cd','rb') as file:
    user_data = pickle.load(file)

real_username = user_data['username']
real_password = user_data['password']

print("Please enter your credentials to move ahead")
username_given = input("Username: ")
password_given = input("Password: ")
if username_given == real_username and password_given == real_password:
    print("Login Successful")

    name = user_data['Name']
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
        print("Enter 2 for some lofi songs(Can help you concentrate)")
        print("Enter 3 to keep a tab on your friends birthday (Can save your friendship)")
        print("Enter 4 to search for a question on google")
        print("Enter 5 to search to search questions regarding your academics.")
        print("Enter 6 to suggest a random song.")
        print("Enter 0 to exit the program")

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
                #TODO: Let the user access and see their journal entry
                subprocess.Popen(["notepad.exe",current_time_use])
            elif response_for_journal == '3':
                print("Deleting all the journal records")
                os.chdir('journals')
                for folder in os.listdir():
                    shutil.rmtree(folder)
                time.sleep(2)
                clear()

        elif response == '2':
            print("Redirecting to Youtube LoFi Stream")
            time.sleep(1)
            webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A")
            clear()

        elif response == '3':
            print("Enter 1 to add an entry")
            print("Enter 2 to see all the entry")
            print("Enter 3 to delete someone's entry")
            print("Enter 4 to delete all the entries")

            bday_response = input("\n>>>")
            if bday_response == '1':
                with open('bdays.cd','rb') as file:
                    to_write = pickle.load(file)

                to_add= True
                while to_add:
                    name = input("Name: ")
                    bday = input("Birthday: ")
                    to_write.update({name:bday})
                    with open('bdays.cd','wb') as file:
                        pickle.dump(to_write,file)
                    print("You wanna continue adding?   #Y for yes and N for no")

                    response = input(">>>")
                    if response.lower() == 'y':
                        to_add = True
                    elif response.lower() == 'n':
                        to_add = False
                    else:
                        print("Invalid respone")
                        time.sleep(1)
            elif bday_response == '2':
                with open('bdays.cd','rb') as file:
                    bday_dict = pickle.load(file)

                name_list = list(bday_dict.keys())
                bday_list = list(bday_dict.values())

                for i in range(len(name_list)):
                    print("{} : {}".format(name_list[i],bday_list[i]))

                response = input("Press any key to return to main menu\n>>>")

            elif bday_response == '3':
                cont = True
                while cont:
                    name = input("Whose record would you like to delete(Case sensitive): ")
                    print("Record Successfully deleted")
                    with open('bdays.cd','rb') as file:
                        bday = pickle.load(file)
                    del bday[name]
                    with open('bdays.cd','wb') as file:
                        pickle.dump(bday,file)
                    print("Do you wanna continue deleting?           #Y for yes, N for no")
                    response = input(">>>")
                    if response.lower() == 'y':
                        continue
                    elif response.lower() == 'n':
                        cont = False
                    else:
                        print("Invalid Response")

            elif bday_response == '4':
                with open("bdays.cd",'wb') as file:
                    empty_dict = {}
                    pickle.dump(empty_dict,file)
                print("Deleted all records")
                time.sleep(2)

        elif response == '4':
            print("So what would you like to search: ")
            query = input(">>>")
            first_website = list(search(query, tld ='co.in', num=1, stop=1, pause=1))[0]
            print("Redirecting you to the first website on google search")
            webbrowser.open(first_website)
            time.sleep(5)

        elif response == '5':
            print("Opening Wolfram Alpha")
            time.sleep(1)
            print("Wolfram Alpha is an AI tool which can be used to solve any problems regarding your academics.")
            time.sleep(2)
            webbrowser.open('www.wolframalpha.com')

        elif response == '6':
            print("You can add your own songs by editing the songs.txt in the directory or remove those you don' want")
            time.sleep(2)
            clear()
            song = give_me_random_song()
            print(song)
            print("Do you want me to open the song on youtube?      #Y for yes and N for no")
            response = input(">>>")
            if response.lower() == 'y':
                print("Opening Song on YouTube")
                findYT(song)
            elif response.lower() == 'n':
                pass
            else:
                print("Invalid Respone")
                time.sleep(1)


        elif response == '0':
            print("Exiting the program")
            time.sleep(1)
            break

        print("Returning back to main Menu")
        time.sleep(1)
        clear()
        continue

#TODO : Encrypt the Journal entry once the user quit the program.

else: #The Else command if the user fails to provide the right password
    print("Invalid Credentials, exiting now")
    time.sleep(2)
    sys.exit()
