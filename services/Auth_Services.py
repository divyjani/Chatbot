
class Auth_Service:
    def __init__(self,email,password):
        self.email=email
        self.password=password  
        
        
    
    def Login(self):
        print("Login Successful",self.email,self.password)
    
    def Register(self,fullname):
        print("Registration Successful",fullname,self.email,self.password)