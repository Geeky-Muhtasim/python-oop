'''
Method Overloading is implemented in different ways.
In simple word, same method with different behaviour.
In python, method overloading doesn't work directly.
'''

class Geometry:

    # def area(self,radius):
    #     return 3.14*radius*radius
    
    # def area(self,l,b):
    #     return l*b

    def area(self,a,b=0):
        if b==0:
            print("Circle", 3.1416*a*a)
        else:
            print("Rectangle", a*b)

obj = Geometry()

obj.area(4)
obj.area(4,5)
