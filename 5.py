import random as r


class Student:
    def __init__(self, name):
        self.name = name
        self.happy = r.randint(10, 100)
        self.progress = r.randint(0, 10)
        self.money = r.randint(100, 500)
        self.alive = True

    def study(self):

        print('Час для навчання')
        self.progress += r.randint(2, 5)
        self.happy -= r.randint(5, 15)

    def sleep(self):

        print('Час для сну')
        self.happy += r.randint(3, 10)

    def chill(self):

        print('Час для відпочинку')
        self.happy += r.randint(15, 30)
        self.money -= r.randint(10, 50)

    def work(self):

        print('Час для роботи')
        self.money += r.randint(50, 150)
        self.happy -= r.randint(5, 20)

    def is_alive(self):

        if self.progress < 2:
            print('Відраховано з інституту через погані оцінки!')
            self.alive = False
        elif self.happy <= 0:
            print('Депресія... Студент покинув навчання!')
            self.alive = False
        elif self.progress > 50:
            print('Вітаю! Ви успішно закінчили навчання!')
            self.alive = False

    def everyday(self):
        print(f"Щастя: {self.happy} | Прогрес: {self.progress} | Гроші: {self.money}")

    def study_life(self, day):
        """Один день із життя студента"""
        print(f"\n День №{day}")

        if self.money < 50:
            self.work()

        elif self.progress < 10:
            self.study()

        else:
            action = r.choice(["study", "sleep", "chill"])
            if action == "study":
                self.study()
            elif action == "sleep":
                self.sleep()
            else:
                self.chill()

        self.everyday()
        self.is_alive()



st1 = Student('Олег')
print(f"Життя студента {st1.name}")

for day in range(1, 366):
    if not st1.alive:
        break
    st1.study_life(day)