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
