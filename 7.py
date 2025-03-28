class Animal:
    def __init__(self, name, age, species, sound):
        self.name = name
        self.age = age
        self.species = species
        self.sound = sound

    def make_sound(self):
        return f"{self.name} каже {self.sound}!"

    def __str__(self):
        return f"{self.species} {self.name}, {self.age} років."

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака", "Гав-гав")
        self.breed = breed

    def __str__(self):
        return super().__str__() + f" Порода: {self.breed}."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Кіт", "Мяу")
        self.color = color

    def __str__(self):
        return super().__str__() + f" Колір: {self.color}."

dog = Dog("Бобік", 3, "Лабрадор")
cat = Cat("Мурчик", 2, "Рудий")

print(dog)
print(dog.make_sound())

print(cat)
print(cat.make_sound())

