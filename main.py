from tkinter import * #Use fome profitable GUI
from auth_manager import AuthManager
from manager import LibraryManager
from db_manager import DataBaseManager


class Main:
    def __init__(self):
        self.auth = AuthManager()
        self.lib_manager = LibraryManager()
        #self.db_manager = DataBaseManager("library.db")

    #Will replace this with GUI
    def main(self):
            while True:
                try:
                    user_input = int(
                                input(
                                    "Enter 1 to to sign-up\n "\
                                    "Enter 2 to login\n"\
                                )
                            )
                    if user_input not in [1,2]:
                        continue
                    else:
                        break
                except:
                    continue
            
            #authenticating user, WORKING CORRECTLY JUST REPLACE THIS WITH GUI  
            data = self.get_data(user_input)
            if user_input == 1:
                is_auth = self.auth.sign_up(data)   
                print("==================================")
                print(is_auth[0])
                print(is_auth[1])
            elif user_input == 2:
                is_auth = self.auth.login(data)
                if is_auth:
                    print("Login successfully!")
                    #Now call library function which shows book details
                    print("==================")
                    #self.lib_manager.view_all_books(self.db_manager)
                else:
                    print("Login failed!")
                    #Either ask for login again till 3 time or stop the app
            

    #Function to get the user data
    def get_data(self,type:int) ->list:
        if type == 1:
            name =  input("Enter your name: ")
            email = input("Enter your email: ")
            __password = input("Enter your password: ")
            age = input("Enter your age: ")
            return [name,email,__password,age,"user"]
        elif type == 2:
            email = input("Enter your email: ")
            __password = input("Enter you password! ")
            return [email,__password]
        

m = Main()
m.main()