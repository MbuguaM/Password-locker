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
    def find_Account(cls,application):
        """ finding the account and returning it """

        for account in cls.accounts_list:
            if account.application == application:
                return account
   
    @classmethod
    def list_all_accounts(cls):
        """ function that return all the accounts """
        for account in cls.accounts_list:
            print(account.application)
            print(account.username)
            print(account.password)
            print("-"*20)
    
    @classmethod
    def delete_account(cls,application):
        """ function that deletes a  given account """
        for account in cls.accounts_list:
            if account.application == application:
                cls.accounts_list.remove(account)
            else:
                return "account for %s doesn't exist"%(application)

    @classmethod
    def gen_lng_password(cls,username):
        for account in cls.accounts_list:
            if account.username == username:
                user=account.username[0:3]
                acct=account.application[0:3]
                symbol=["@","#","%","*","~","!","$","£"]
                number=["1","2","3","4","5","6", "7","8","9"]
                lng_password=(choice(symbol) + acct + choice(number) + user + choice(symbol) + acct + choice(number) + user) 
                account.password = lng_password
    
    @classmethod
    def gen_shrt_password(cls,username):
        for account in cls.accounts_list:
            if account.username == username:
                user=account.username[0:3]
                symbol=["@","#","%","*","~","!","$","£"]
                shrt_password=(choice(symbol) + user)
                account.password = shrt_password
    