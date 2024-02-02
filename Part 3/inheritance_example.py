class Phone:
    def __init__(self,price,brand,camera):
        print("Inside the constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying the phone")

class Smartphone(Phone):
    
    def buy(self):
        print("Buying the smartphone")

'''
Child class can acquire the constructor of Parent class.
But it can't access the private attributes of parent class.
'''


s = Smartphone(20000, 'Samsung', 20)
print(s.brand,s.camera)

'''
Here, the buy function will execute the method
of the smartphone class. As s refers to the object of Smartphone
class. So, it shall execute the buy method from its own class.
This is also called method overriding.
'''

s.buy()