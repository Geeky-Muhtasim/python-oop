class Phone:
    def __init__(self,price,brand,camera):
        print("Inside the constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

class Smartphone(Phone):
    pass

'''
Child class can acquire the constructor of Parent class.
But it can't access the private attributes of parent class.
'''


s = Smartphone(20000, 'Samsung', 20)
print(s.brand,s.camera)