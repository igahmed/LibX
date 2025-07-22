from db_manager import DataBaseManager

#Contain constructor, sign_up,login,logout,and is_admin functions
class AuthManager:
    def __init__(self):
        self.db = DataBaseManager("library.db")
        self.current_user = None
    

    #Functon is used to sign-up in the app 
    def sign_up(self,name:str,email:str,password:str,age:int,role="user")->tuple[bool,str]: 
        #Checking if the user exist in the database or not 
        existing_user = self.db.get_user_by_email(email)
        if existing_user:
            return False, "User already Exist"
        if self.db.add_user(name,email,password,age,role):
            return True, "User registered successfully"
        else:
            return False, "Registeration Failed"
        

    #login function
    def login(self,email: str,password: str) ->bool:
        #Retriving user info based on email to authenticate the user
        user = self.db.get_user_by_email(email)
        if not user:
            return False
        if user[3] == password:
            self.current_user = {
                'id': user[0],
                'name': user[1],
                'email': user[2],
                'role': user[5]
            }
            return True
        else: 
            return False


    def logout(self) -> None:
        self.current_user = None

    
    def is_admin(self) ->bool:
        if self.current_user and self.current_user['role'] == "admin":
            return True
        return False