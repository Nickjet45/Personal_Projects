import os
import time

# List of emails to add to text file
email_list = ['YouGotTested@gmail.com', 'Test@gmail.com', 'YahooSucks@gmail.com', 'MichaelBad@gmail.com']


def Email_Check():
    # Creates variable that list all files in directory
    list_of_files = os.listdir()

    # Checks to see if 'Email_list' exists in current directory
    # If it exists then do nothing else
    # Create the file
    if 'Email_list' in list_of_files:
        print('Checking email list.... ')
    else:
        print('Creating email list... ')
        time.sleep(1)
        checker = open('../Pycharm Projects/Email_list', 'a+')
        checker.close()

    # Opens Email_list
    check = open('../Pycharm Projects/Email_list')

    # Runs through every email in the email_list array
    for email in email_list:

        # If the email in the array already exists in the text file
        # Print saying which email is already in there
        if email in check.readline():
            print(email + ' already in list')

        # Else add the email to the text file
        # Print stating which email was added to the file
        else:
            Email_Add(email)
            print(email + ' has been added to list')
    check.close()


def Email_Add(email):
    # Opens 'Email_list' file and adds the passed through email
    # Does not check to see if the email already exists
    add = open('../Pycharm Projects/Email_list', "a+")
    add.write(email + ',' + '\n')
    add.close()


Email_Check()
