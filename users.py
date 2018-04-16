import pyperclip

class User:
    
    """ stores the new instances of users """
    
    user_list=[]
     
    def __init__(self,fullName, email,username,password):
        self.fullName = fullName
        self.email = email
        self.username = username
        self.password = password

    def saveUser(self):
        """storing the new user instance"""
        User.user_list.append(self)
    
    @classmethod
    def find_user(cls,username):
        """ find the user is stored in the array """
        for user in cls.user_list: 
            if user.username == username:
                return user 
                
    @classmethod
    def user_exists(cls,username):
        """ find if user exists """
        for user in cls.user_list: 
            if user.username == username:
                return True
            else:
                return False