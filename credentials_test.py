import unittest # Importing the unittest module
from credentials import Credentials # Importing the account class


class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Cate","Nduku","Cate1234","catenduku995@gmail.com")# create Account object

    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name,"Cate")
        self.assertEqual(self.new_credentials.usr_name,"Nduku")
        self.assertEqual(self.new_credentials.password,"Cate1234")
        self.assertEqual(self.new_credentials.email,"catenduku995@gmail.com")
        
    def test_save_credentials(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_credentials.save_credentials() # saving the new account
        self.assertEqual(len(Credentials.credentials_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []        
