#!/usr/bin/env python3.6
from account import Account
from credentials import Credentials
import random

def create_account(account_name,user_name,password,email):
    '''
    Function to create a new account
    '''
    new_account = Account(account_name,user_name,password,email)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()    

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()    
def find_account(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Account.find_by_name(name)    

def check_existing_accounts(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Account.account_exist(name)    

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts() 
 
def create_credentials(credentials_name,usr_name,password,email):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(credentials_name,usr_name,password,email)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save account
    '''
    credentials.save_credentials()
    
def del_credentials(credentials):
    '''
    Function to delete a account
    '''
    credentials.delete_credentials()  
    
def find_credentials(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Credentials.find_by_name(name)    

def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)    

def display_credentials():  
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_credentials() 



def main():
    
    print("Welcome to your Password Locker, choose your path from the list of allowed actions")

    while True:
        print("Allowed Actions: \n ad - create a new user account with a user-defined password\n ag - create a new user account with a auto-generated password\n da - display all user accounts \n ex -exit the contact list \n")

        short_code = input().lower()

        if short_code == 'ad':
            print("New User")
            print("-"*10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ...")
            user_name = input()

            print("Enter Password ...")
            pword = input()

            save_accounts(create_account(f_name, l_name, p_number, e_address))  # create and save new user account.
            save_credentials(create_credentials(user_name, pword, e_address))  # create and save a credential listing for the above user
            print('\n')
            print(f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
            print('\n')

        elif short_code == 'ag':
            print("New User")
            print("-" * 10)
            print("Hey There!!! What site do you want to create an account for?")
            site = input()
            print(f"Aah!! So you love {site}?")

            print("First name ....")
            f_name = input()
     
            print("Last name ...", )
            l_name = input()

            print("Phone number ...")
            p_number = input()

            print("Email address ...")
            e_address = input()

            print("Enter username ... Hint: a secure password will be generated for you...")
            user_name = input()

            s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
            pword = "".join(random.sample(s, 8))

            save_accounts(create_credentials(f_name,l_name,p_number,e_address))  # create and save new user account.
            save_credentials(create_credentials(user_name, pword, e_address))  # create and save a credential listing for the above user
            print('\n')
            print(f" A new {site} account by {f_name} {l_name} has successfully been created")
            print(f" The username is {user_name} and the password is {pword}")
            print('\n')

        