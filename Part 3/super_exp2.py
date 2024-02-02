class Phone:

    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print("Buying phone")

class SmarterPhone(Phone):

    def __init__(self,price,brand,camera, os, ram):
        print("First in child")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")

s = SmarterPhone(40000, "Xiaomi", 50, "Android", 8)

print(s.os)

print(s.brand)

s.buy()