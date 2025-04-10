class A:
    def greet(self): print("A")

class B(A):   #child class 1
    # def greet(self): print("B")
    pass

class C(A):  #child class 2
    # def greet(self): print("C")
    pass

class D(B, C): pass   #child class which inherits from two other child classes....

D().greet() 


print(D.__mro__)

