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
    
    def text_saveAccount(self):
        """ confirming if the account has been saved """
        self.new_account.saveAccount()
        self.assertEqual(len(Account.accounts_list),1)
    
    def test_check_Account_Exists(self):
        """ confirms that the given account exists """
        self.new_account.saveAccount()
        test_account=Account("facebook","Mbout","")
        test_account.saveAccount()
        
        foundAccount= Account.check_Account_Exists("facebook")
        self.assertTrue(foundAccount)

    
    def test_findAccount(self):
        """ find the account and returns it """
        self.new_account.saveAccount()
        test_account=Account("facebook","Mbout","")
        test_account.saveAccount()
        
        foundAccount=Account.findAccount("facebook")
        self.assertEqual(foundAccount, test_account.application)

    def test_gen_lng_password(self):
        """ checking if the password has been created """
        lng_password= Account.gen_lng_password("MbuguaM","facebook")
     
        self.assertTrue(len(lng_password),8)
    def test_gen_shrt_password(self):
        """ checking if the short password has been created """

        shrt_password=Account.gen_shrt_password("MbuguaM")
        self.assertTrue(len(shrt_password),4)

if __name__ == "__main__":
    unittest.main()   
