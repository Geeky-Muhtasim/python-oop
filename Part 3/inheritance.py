class User:

    def login(self):
        print("Login")
    def register(self):
        print("Register")

class Student(User):  #Here, student is the subclass of User class

    def enroll(self):
        print("Enroll")
    
    def review(self):
        print("Review")

std1 = Student()

std1.login()
std1.register()
std1.enroll()
std1.review()


user1 = User()

'''
user1.enroll() Here, the super class can't 
access the properties of sub class.
'''