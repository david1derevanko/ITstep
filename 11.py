#class Animal:
#    def sound(self):
#        pass
#
#class Dog(Animal):
#    def sound(self):
#            return "ГАВ"
#
#class Cat(Animal):
#    def sound(self):
#                return "MЯУ"
#
#class Cow(Animal):
#    def sound(self):
#                    return "MY"
#
#def speak(an):
#    print(an.sound())
#a1=Dog()
#a2=Cat()
#a3=Cow()
#speak(a1)
#speak(a2)
#speak(a3)


#class Pay:
#    def process(self,money):
#        pass
#class Credit(Pay):
#    def process(self,money):
#        return "Оплата"+str(money)+ "грн здійснена через кредитну картку"
#class Cash(Pay):
#    def process(self,money):
#        return "Оплата"+str(money)+ "грн здійснена через готівку"
#class System(Pay):
#    def process(self,money):
#        return "Оплата"+str(money)+ "грн здійснена через онлайн систему"
#buy=[Credit(),Cash(),System()]
#num=int(input('Введіть суму покупки: '))
#for k in buy:
#    print(k.process(num))


#class Dog:
#    def __init__(self,name):
#        self.name=name
#dog1=Dog("Бані")
#print(dog1.name)

#class Dog:
#    def __init__(self,name):
#        self.name=name
#        self.__age=2
#    def info(self):
#        return self.__age
#dog1=Dog("Бані")
#print(dog1.info())

#class Dog:
#    def __init__(self,name):
#        self._bread="бульдог"
#class D (Dog):
#    def info(self):
#        return "Це щеня породи"+self._bread
#dog1=D("Бані")
#print(dog1.info())

#class Person:
#    def __init__(self,name,age,salary):
#        self.name=name
#        self._age=age
#        self.__salary=salary
#    def info(self):
#        print("Вітаю. Мене звати",self.name)
#        self._infoAge()
#        self.__infoSalary()
#    def _infoAge(self):
#        print('Мій вік', self._age)
#    def __infoSalary(self):
#       print('Моя ЗП', self.__salary)
#
#class Employee(Person):
#    def __init__(self, name, age, salary,pos):
#         super().__init__(name,age,salary)
#         self.pos=pos
#    def printInfo(self):
#        print('Моя посада', self.pos)
#        print('Мій вік', self._age)
#        print('Моя ЗП', self.__salary)
#human=Person('Олеся', 20,2000)
#emp=Employee('Петро',25,45000, 'інженер')
#print(human.name)
#human.info()
#print(emp.name)
#emp.printInfo()
#print(emp._age)

import random as r


class Character:
    def __init__(self, name, health):
        self.__name = name
        self.__health = max(0, health)

    def attack(self):
        raise NotImplementedError("Цей метод повинен бути реалізований у дочірньому класі.")

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)
        print(f"{self.__name} отримав {amount} шкоди!")

    def is_alive(self):
        return self.__health > 0

    def __str__(self):
        return f"{self.__name}, моє здоров'я: {self.__health}"

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150)

    def attack(self):
        return f"{self._Character__name} атакує мечем!"

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 100)

    def attack(self):
        return f"{self._Character__name} атакує магією!"


class LibraryItem:
    def __init__(self, title, author, item_id):
        self.__title = title
        self.__author = author
        self.__item_id = item_id
        self.__is_borrowed = False

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_item_id(self):
        return self.__item_id

    def is_same_item(self, other_item):
        return self.__item_id == other_item.get_item_id()

    def borrow_item(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False

    def display_info(self):
        raise NotImplementedError("Цей метод повинен бути реалізований у дочірньому класі.")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, pages):
        super().__init__(title, author, item_id)
        self.__pages = pages

    def display_info(self):
        print(f"Книга: {self.get_title()}, Автор: {self.get_author()}, Сторінки: {self.__pages}")

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, issue_number):
        super().__init__(title, author, item_id)
        self.__issue_number = issue_number

    def display_info(self):
        print(f"Журнал: {self.get_title()}, Автор: {self.get_author()}, Номер випуску: {self.__issue_number}")

class Audiobook(LibraryItem):
    def __init__(self, title, author, item_id, duration):
        super().__init__(title, author, item_id)
        self.__duration = duration

    def display_info(self):
        print(f"Аудіокнига: {self.get_title()}, Автор: {self.get_author()}, Тривалість: {self.__duration} хвилин")


if __name__ == "__main__":
    hero = Warrior("Герой")
    print(hero)

    for _ in range(5):
        hero.take_damage(r.randint(5, 20))
        print(hero)

    library_items = [
        Book("Майстер і Маргарита", "М. Булгаков", 1, 320),
        Magazine("Наука і життя", "Редакція", 2, 45),
        Audiobook("1984", "Дж. Орвелл", 3, 640)
    ]

    for item in library_items:
        item.display_info()

    book1 = Book("Захар Беркут", "І. Франко", 10, 200)
    book2 = Book("Захар Беркут", "І. Франко", 10, 200)
    print("Чи однакові об'єкти?", book1.is_same_item(book2))
    print("Чи можна взяти книгу:", book1.borrow_item())
    print("Повторне взяття:", book1.borrow_item())
    print("Повернення книги:", book1.return_item())

