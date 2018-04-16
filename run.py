from users  import User
from account import Account 
import pyperclip

def create_user(fullName,email,username,password):
    """ creating a new user """
    newUser= User(fullName,email,username,password)

    return newUser

def saveUser(newUser):
    """ saving the created user """
    newUser.savUser()

def User_exists(username):
    """ checking if the user has been added """
    return  User.user_exists(username)

def find_user(username):
    """ retreving the user """
    return  User.find_user(username)

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

            print("Password.....")
            password = input()
            new = create_user(fullname, email, username, password)
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
                            break

                                # insert credentials logic here
                                # while True:
                                #     break
                                
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
