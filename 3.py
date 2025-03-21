class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"



car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

print(car1.get_info())
print(car2.get_info())