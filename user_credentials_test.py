from user import User
from user import Credential
import unittest
import pyperclip


class TestUser(unittest.TestCase):
   
	def setUp(self):
		
		self.new_user = User("Cate","Nduku","abc123")

	def test__init__(self):
		
		self.assertEqual(self.new_user.first_name,'Cate')
		self.assertEqual(self.new_user.last_name,'Nduku')
		self.assertEqual(self.new_user.password,'abc123')

	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User("Cate","Nduku","abc123")
		self.new_user.save_user()
		user2 = User('Joyce','Mueni','pswd100')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('  Cate','Facebook','CateNduku','abc123')

	def test__init__(self):
		'''
		Test to if check the initialization/creation of credential instances is properly done
		'''
		# self.assertEqual(self.new_credential.user_name,'Cate')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'CateNduku')
		self.assertEqual(self.new_credential.password,'abc123')

	def test_save_credentials(self):
		'''
		Test to check if the new credential info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Cate','Twitter','CateNduku','pswd100')
		twitter.save_credentials()
		self.assertEqual(len(Credential.credentials_list),2)

	

	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Cate','Twitter','CateNduku','abc123')
		twitter.save_credentials()
		gmail = Credential('Cate','Instagram','CateNduku','abc123')
		gmail.save_credentials()
		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)

	def test_find_by_site_name(self):
		'''
		Test to check if the find_by_site_name method returns the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Cate','Twitter','CateNduku','abc123')
		twitter.save_credentials()
		credential_exists = Credential.find_by_site_name('Twitter')
		self.assertEqual(credential_exists,twitter)

	def test_copy_credential(self):
		'''
		Test to check if the copy a credential method copies the correct credential
		'''
		self.new_credential.save_credentials()
		twitter = Credential('Jane','Twitter','maryjoe','abc123')
		twitter.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential =Credential.find_by_site_name(credential.site_name)
				return pyperclip.copy(find_credential.password)
		Credential.copy_credential(self.new_credential.site_name)
		self.assertEqual('abc123',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity=2)