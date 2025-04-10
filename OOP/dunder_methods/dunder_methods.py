class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price!r})"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __add__(self, other):
        return self.price + other.price



p1 = Product("Laptop", 50000)
p2 = Product("Tablet", 25000)
p3 = Product("Laptop", 50000)

print(str(p1))    
print(repr(p1))    

print(p1 == p3)   
print(p1 < p2)     

print(p1 + p2)    





#There are more than 100 magic methods , that can be implemented....