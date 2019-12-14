#!/usr/bin/env python3.6
from account import Account
from credentials import Credentials

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
