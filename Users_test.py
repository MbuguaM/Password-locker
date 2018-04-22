import unittest
from users import User
import pyperclip

class TestUser(unittest.TestCase):

    def setUp(self):
        """ assing a test instance of the class"""
        self.new_user= User("MbuguaMunga","Munga2mbugua@gmail.com","MbuguaM","Mine2")


    def tearDown(self):
        """ reseting the array """
    
        User.user_list=[]

    def test_init(self):
        """ confirming that all the class instance have saved the information passed """
    
        self.assertEqual(self.new_user.fullName, "MbuguaMunga") 
        self.assertEqual(self.new_user.email,"Munga2mbugua@gmail.com")
        self.assertEqual(self.new_user.username,"MbuguaM")
        self.assertEqual(self.new_user.password,"Mine2")

    def test_saveUser(self):
        """ checking if the user has been saved """
        self.new_user.saveUser()
        self.assertEqual(len(User.user_list),1)

    def test_find_user(self):  
        """ finding if the user exists """

        self.new_user.saveUser()
        test_user=User("ManDavis","davis@gmail","dave","d21")
        test_user.saveUser()

        foundUser=User.find_user("dave") 
        self.assertEqual(foundUser.password,test_user.password)

    def test_user_exists(self):
        """ confirming tha the user actually exists """
        self.new_user.saveUser()
        test_user=User("ManDavis","davis@gmail","dave","d21")
        test_user.saveUser()

        user=User.user_exists("MbuguaM") 
        self.assertTrue(user)

if __name__ == '__main__':
    unittest.main()