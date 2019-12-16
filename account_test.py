import unittest # Importing the unittest module
from account import Account # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account(
            'Cate', 'Nduku', 'catenduku995@@gmail.com', '0701646673', 'abc1234')

    def test__init__(self):
        self.assertEqual(self.new_account.first_name, 'Cate')
        self.assertEqual(self.new_account.last_name, 'Nduku')
        # self.assertEqual(self.new_account.email, 'catenduku995@gmail.com')
        self.assertEqual(self.new_account.phone_number, '0701646673')
        self.assertEqual(self.new_account.password, 'abc1234')

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []    
   
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account('Cate', 'Nduku', 'catenduku995@@gmail.com', '0701646673', 'abc1234') # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove an account from our account list
            '''
            self.new_account.save_account()
            test_account = Account('Cate', 'Nduku', 'catenduku995@@gmail.com', '0701646673', 'abc1234') # account
            test_account.save_account()

            self.new_account.delete_account()# Deleting an account object
            self.assertEqual(len(Account.account_list),1) 

    # def test_find_name(self):
    #     '''
    #     test to check if we can find an account by account_name and display information
    #     '''

    #     self.new_account.save_account()
    #     test_account = Account('Cate', 'Nduku', 'catenduku995@@gmail.com', '0701646673', 'abc1234') # new account
    #     test_account.save_account()

    #     find_account = Account.find_by_name("Test")

    #     self.assertEqual(find_account.email,test_account.email)  
          
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account('Cate', 'Nduku', 'catenduku995@@gmail.com', '0701646673', 'abc1234') # new account
        test_account.save_account()

        account_exists = Account.account_exist("abc1234")

        self.assertTrue(account_exists)
        
        
    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''
        displayed = Account.display_accounts()
        self.assertEqual(displayed,Account.account_list)    

if __name__ == '__main__':
    unittest.main()