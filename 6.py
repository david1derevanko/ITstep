#class Human:
#    count=0
#
#    def __unit__(self,name="Vasya"):
#        self.name=name
#        Human.count+=1
#class Auto:
#    def __unit__(self,brand):
#        self.brand = brand
#        self.passenger=[]
#    def add(self,*args):
#        for n in args:
#            self.passenger.append(n)
#    def info(self):
#        if self.passenger==[]:
#            print('Пасажири відсутні у ',self.brand)
#        else:
#            print('Пасажири присутні у ',self.brand,": ")
#            for n in self.passenger:
#                print(n.name)
#
#pas1=Human()
#pas2=Human('Tanya')
#pas3=Human('Sacha')
#car1=Auto('Bogdan')
##car1.add(pas1)
##car1.add(pas2)
#car1.add(pas1,pas2,pas3)
#car1.info()
#print(Human.count)

#class Human:
#    def __init__(self, name, age, height, city, animal):
#        self.name = name
#        self.age = age
#        self.height = height
#        self.city = city
#        self.animal = animal
#
#    def __str__(self):
#        return f'Вітаю! Я {self.name}, мені {self.age} років. Я з міста {self.city}. Маю зріст {self.height} см, я маю тварин: {self.animal}.'
#
#class Pupil(Human):
#    def __init__(self, name, age, height, city, animal, school, clas):
#        super().__init__(name, age, height, city, animal)
#        self.clas = clas
#        self.school = school
#
#    def __str__(self):
#        return super().__str__() + f' Навчаюсь у школі {self.school} в {self.clas} класі.'
#
#class Worker(Human):
#    def __init__(self, name, age, height, city, animal, job, salary):
#        super().__init__(name, age, height, city, animal)
#        self.job = job
#        self.salary = salary
#
#    def __str__(self):
#        return super().__str__() + f' Працюю на посаді {self.job}, маю зарплату {self.salary} $.'
#
#h = Human('Masha', 12, 156, 'Запоріжжя', 'Кіт')
#p = Pupil('Oleg', 14, 170, 'Дніпро', 'Собака', 101, 9)
#w = Worker('Yana', 35, 168, 'Львів', 'Кіт', 'дизайнер', 3500)


#print(h)
#print(p)
#print(w)

class PC:
    def __init__(self,model="HP"):
        super().__init__()
        self.model=model
        self.memory=256
class Display:
    def __init__(self):
        super().__init__()
        self.res='4k'
class  Smart(PC,Display):
    def info(self):
        print('Смартфон моделі',self.model,"має об'єм пам'яти",self.memory,'Мб та розширення екрана', self.res)

tel=Smart('Samsung')
tel.info()
