class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} engine started.")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start(self):
        super().start()
        print(f"{self.model} is ready to drive..")

c = Car("tata", "curvv")
c.start()
