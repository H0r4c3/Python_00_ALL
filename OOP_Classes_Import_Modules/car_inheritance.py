
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def describe(self):
        print(f"The {self.color} car has {self.mileage} miles.")


blue_car = Car("blue", 20000)
red_car = Car("red", 30000)

blue_car.describe()
red_car.describe()

class Dacia(Car):
    def __init__(self, color, mileage, age):
        super().__init__(color, mileage)
        self.age = age
    

dacia_car = Dacia("black", 1000000, 100)
dacia_car.describe()