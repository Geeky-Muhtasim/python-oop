
'''
Super example
'''

class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")

        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying phone")

class Smartphone(Phone):
    '''
For method over riding this buy method will be executed. 
'''
    def buy(self):
        print("Buying Smartphone")
        super().buy()

        '''
        This super() means it'll access to the buy method of the parent class.
        It can access all the methods of the parent class as well.
        '''

s = Smartphone(50000, "Apple", 12)

s.buy()