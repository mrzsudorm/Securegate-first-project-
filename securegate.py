
class LoginSystem:

    def __init__(self, username, password):
        self.username = username
        self.password = password
    def authenticate(self):
        if self.username == "Tyler Durden" and self.password == "Project Mayhem":
            print("\nLogin Successful!")
            print("Welcome to fight club.")
        else:
            print("\nLogin Failed!")
            print("Invalid username or password.")


username = input("Enter the Username: ")
password = input("Enter the Password: ")


user1 = LoginSystem(username, password)



user1.authenticate()
