class Dog:
    
    def __init__(self, name, breed):  # Constructor
        self.name = name             # Attribute
        self.breed = breed

    def bark(self):                  # Method
        print(f"{self.name} says Woof!")
        

dog = Dog("buddy","husky")

dog.bark()

dog2 = Dog("buddy2","goldie")
dog2.bark()

