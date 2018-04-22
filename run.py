from users  import User
from account import Account 
import pyperclip

def create_user(fullName,email,username,password):
    """ creating a new user """
    newUser= User(fullName,email,username,password)

    return newUser

def saveUser(newUser):
    """ saving the created user """
    newUser.saveUser()

def User_exists(username):
    """ checking if the user has been added """
    return  User.user_exists(username)

def find_user(username):
    """ retreving the user """
    return  User.find_user(username)

def create_account(application,username):
    """ funtion that creates an account """
    new_account = Account(application,username,"")
    new_account.saveAccount();
def list_all_accounts():
    """ function  to list all the accounts"""
    return Account.list_all_accounts()
def create_long_password(username):
    """creates a long password """
    Account.gen_lng_password(username)
def create_shrt_password(username):
    """ creates a short password """
    Account.gen_shrt_password(username)
def delete_account(application):
    """ deleting an account """
    return Account.delete_account(application)
def main():
    print("welcome to passwordlocker")
    print("-" *10)
    
    while True:
        print("Please use the following short codes:")
        print('\n')
        print ("su - Sign-up, li - Login", "ex - Exit")

        short_code = input().lower()

        if short_code == 'su':
            print("Sign up to create a PassLocker account")
            print("-"*20)

            print("Fullname.....")
            fullname = input()

            print("Email Address.....")
            email = input()

            print("Username.....")
            username = input()
            
            print("password.....")
            password = input()
            new = create_user(fullname, email, username,password)
            saveUser(new)
            print('\n')
            print("Welcome %s, your account has sucessfully been created" %(username))
            print ('\n')

        elif short_code == 'li':
            print("Login to your PassLocker account")
            print("-"*20)

            while True:

                print("Username.....")
                search_user = input()
                if User_exists(search_user):
                    search_user = find_user(search_user)
                    while True:
                        print("Password.....")
                        password = input()
                        if password == search_user.password:
                            print(" %s Welcome, you are logged in!" %(username))
                            # give more options such as search for agiven account see the account that exists
                            print("please use the short codes")
                            print("li- list all the accounts present, ad- add an account,del - delete an account, ex - exit")
                            short_code = input().lower()
                            if short_code == "li":
                                # list all the accounts
                                list_all_accounts()
                            elif short_code == "ad":
                                #create a new account
                                print("%s create an account for which you need to generate a password" %(username))
                                print("-"*20)

                                print("Enter Account name.....")
                                account = input()

                                print("Enter Account username .......")
                                username = input()
                                
                                create_account(account,username)

                                while True:
                                    print("Please use short codes")
                                    print("lg - generate long password, sh - generate short password, ex - exit")
                                    
                                    short_code =input().lower()

                                    if short_code == "lg":
                                        create_long_password(username)
                                    elif short_code == "sh":
                                        create_shrt_password(username)
                                    elif short_code == "ex":
                                        break
                                    else:
                                        print("please ener a valid short code:")
                            elif short_code == "del":
                                print("Enter accountname...")
                                account_name = input()
                                
                                delete_account(account_name)
                            elif short_code == "ex":
                                # break out of the loop
                                break
                            else:
                                print("please enter a valid short_code")
                            
                                 
                        else:
                            print("Incorrect password")
                            print ('\n')
                    break
                else:
                    print(" %s does not exist, please sign up." %(username))
        elif short_code == 'ex':
            print("Bye .......")
            break
        else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
