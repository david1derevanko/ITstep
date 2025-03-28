class Transport:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed  # км/год

    def move(self, distance):
        time = distance / self.speed  # Час у годинах
        return f"{self.name} подолає {distance} км за {time:.2f} год."

    def __str__(self):
        return f"{self.name} рухається зі швидкістю {self.speed} км/год."

class Car(Transport):
    def __init__(self, name, speed, brand):
        super().__init__(name, speed)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f" Марка: {self.brand}."

class Bicycle(Transport):
    def __init__(self, name, speed, type_bike):
        super().__init__(name, speed)
        self.type_bike = type_bike

    def __str__(self):
        return super().__str__() + f" Тип: {self.type_bike}."

class Plane(Transport):
    def __init__(self, name, speed, airline):
        super().__init__(name, speed)
        self.airline = airline

    def __str__(self):
        return super().__str__() + f" Авіакомпанія: {self.airline}."


car = Car("Автомобіль", 120, "Toyota")
bicycle = Bicycle("Велосипед", 25, "Гірський")
plane = Plane("Літак", 900, "UkrAir")

print(car)
print(car.move(240))

print(bicycle)
print(bicycle.move(50))

print(plane)
print(plane.move(1800))