class Account:
    """
    Class that generates new instances of users.
    """
    account_list = []  # empty account list

    def __init__(self, first_name, last_name, email, phone_number, password):
        '''
        Method to define the properties for each user object will hold.
        '''
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def find_by_name(cls, name):
        for account in cls.account_list:
             if account.account_name == name:
                return account

    @classmethod
    def account_exist(cls, name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.password == name:
                return account

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list
