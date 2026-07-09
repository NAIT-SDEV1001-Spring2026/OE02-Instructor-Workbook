class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"A {self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Car(make='{self.make}',model='{self.model}',year={self.year})"
    
    def Honk(self):
        print(f"{self.make} {self.model} says beep beep!")

class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def list_cars(self):
        for car in self.cars:
            print(car)


garage = Garage()
my_car = Car('Honda', 'Civic', 1996)
my_other_car = Car('Toyota', 'Corolla', 2015)
garage.add_car(my_car)
garage.add_car(my_other_car)
print(f'The make of my car is: {my_car.make}')
my_car.Honk()
my_other_car.Honk()
garage.list_cars()
print(repr(my_car))