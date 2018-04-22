from random import choice
from account import Account


accounts_list = []

def create_accounts():
    new_account = Account("twitter","Someone","")
    second_account = Account("facebook", "thrift","")
    accounts_list.append(second_account)
    accounts_list.append(new_account)
    return accounts_list

print(create_accounts())
def gen_lng_password():
    for account in accounts_list:
        if account.username == username:
            user=account.username[0:3]
            acct=account.application[0:3]
            symbol=["@","#","%","*","~","!","$","£"]
            number=["1","2","3","4","5","6", "7","8","9"]
            lng_password=(choice(symbol) + acct + choice(number) + user + choice(symbol) + acct + choice(number) + user) 
            account.password = lng_password
       

gen_lng_password("thrift")

def shown():
    for account in accounts_list:
        if account.username == "thrift":
            print(account.password)
            print(len(account.password))
        else:
            break

shown()