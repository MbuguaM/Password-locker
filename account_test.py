import unittest
from account import Account
import pyperclip

class AccountTest(unittest.TestCase):
    """ This test that the class funtions """

    def setUp(self):
        """ initializes a new instance of the accounts class"""
        self.new_account= Account("Twitter","MbuguaM","")
    
    def tearDown(self):
        """ clears out the class array """
        Account.accounts_list=[]


    def test_init(self):
        """ confirms tha the values passed were added """
        self.assertEqual(self.new_account.application,"Twitter")
        self.assertEqual(self.new_account.username,"MbuguaM")
        self.assertEqual(self.new_account.password,"")
    
    def test_saveAccount(self):
        """ confirming if the account has been saved """
        self.new_account.saveAccount()
        self.assertEqual(len(Account.accounts_list),1)
    
    def test_check_Account_Exists(self):
        """ confirms that the given account exists """
        self.new_account.saveAccount()
        # trial_account = Account("Facebook","Mbout","None")
        trial_account = Account("Facebook","MbuguaM","")
        # trial_account.saveAccount()
        trial_account.saveAccount()

        foundAccount= Account.check_Account_Exists("Twitter")
        self.assertTrue(foundAccount)

    
    def test_find_Account(self):
        """ find the account and returns it """
        self.new_account.saveAccount()
        test_account=Account("facebook","Mbout","")
        test_account.saveAccount()
        
        foundAccount=Account.find_Account("facebook")
        self.assertEqual(foundAccount, test_account)

    def test_gen_lng_password(self):
        """ checking if the password has been created """
        self.new_account.saveAccount()
        test_account=Account("facebook","Mbout","")
        test_account.saveAccount()
        Account.gen_lng_password("Mbout")
     
        self.assertTrue(len(test_account.password),16)

    def test_gen_shrt_password(self):
        """ checking if the short password has been created """
        
        self.new_account.saveAccount()
        test_account=Account("facebook","Mbout","")
        test_account.saveAccount()
        Account.gen_shrt_password("MbuguaM")
        self.assertTrue(len(self.new_account.password),4)
    
    def test_deleted_account(self):
        """checking is funtion deletes a given account"""
        self.new_account.saveAccount()
        test_account=Account("facebook","Mbout","")
        test_account.saveAccount()
        
        self.assertEqual(len(Account.accounts_list),2)
        Account.delete_account("Twitter")
        self.assertEqual(len(Account.accounts_list),1)
if __name__ == "__main__":
    unittest.main()   
