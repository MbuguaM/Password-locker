import pyperclip
from random import choice 

class Account:
    """ stores the accounts and their corresponding passwords """
    accounts_list=[]

    def __init__(self,application,username,password):
       
        self.application = application
        self.username = username
        self.password = password
    
    def saveAccount(self):
        """ save the accounts intance to the array """
        Account.accounts_list.append(self)

    @classmethod
    def check_Account_Exists(cls,application):
        """ checking the array for the account"""
        for account in cls.accounts_list:
            if account.application == application:
                return True
            else:
                return False

    @classmethod
    def findAccount(cls,application):
        """ finding the account and returning it """

        for account in cls.accounts_list:
            if account.application == application:
                return account
   
    @classmethod
    def gen_lng_password(cls,username,application):
        for account in cls.accounts_list:
            user=account.username[0:3]
            acct=account.application[0:3]
            symbol=["@","#","%","*","~","!","$","£"]
            number=["1","2","3","4","5","6", "7","8","9"]
            lng_password=(choice(symbol) + acct + choice(number) + user) 
            return lng_password
    
    @classmethod
    def gen_shrt_password(cls,username):
        for account in cls.accounts_list:
            user=account.username[0:3]
            symbol=["@","#","%","*","~","!","$","£"]
            shrt_password=(choice(symbol) + user)
            return shrt_password 
    