class Atm:

    # _init_  Constructor 
    '''
    Constructor is a special method defined
    inside the class of whose the code 
    inside it executes automatically.
    
    '''
    def __init__(self):
        self.pin = ''
        self.balance = 0

        self.menu()

    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Bye")    

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin set successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter your amount"))
            self.balance = self.balance + amount
            print('Deposit Successful')
            self.menu()
        else:
            print("Invalid Pin")
            self.menu()
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdrawl Successful")
                self.menu()
            else:
                print("Insufficient Fund")
                self.menu()
        else:        
            print("Insufficient Balance")
            self.menu()

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print(self.balance)
            self.menu()
        else:
            print("invalid pin")
            self.menu()