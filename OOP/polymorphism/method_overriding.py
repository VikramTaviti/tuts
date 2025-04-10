class Animal:
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def announce(animal: Animal):
    print(animal.speak())

announce(Dog())  
announce(Cat())  
