import unittest # Importing the unittest module
from account import Account # Importing the account class


class TestAccount(unittest.TestCase):
    def setUp(self):
       
        self.new_account = Account("Facebook","Nduku","Cate1234","catenduku995@gmail.com") # create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Facebook")
        self.assertEqual(self.new_account.user_name,"Nduku")
        self.assertEqual(self.new_account.password,"Cate1234")
        self.assertEqual(self.new_account.email,"catenduku995@gmail.com")
