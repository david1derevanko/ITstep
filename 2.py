#class Car:
    #speed=115
    #def __init__(self,speed_car):
            #self.speed=speed
    #def info(self):
        #print("Швідкість авто: ",self.speed)
#sp=int(input('Максимальна Швидкість авто: '))
#auto=Car()
#print("Швідкість авто: ",self.speed)
#auto.info()
#auto2=Car(180)
#auto2.info()


# class Pupils:
#     count=0
#     def __init__(self,name,height):
#         self.name=name
#         self.name=name
#         Pupils.count+=1
#     def show(self):
#         print("Ім'я участника:", self.name,"Зріст:", self.height)
#     def__bool__(self):
#         return self.name!=None
#     def__len__(self):
#     return self.height
#
# p1=Pupils("Ігор",155)
# p1.__str__()
# p2=Pupils("Oля",158)
# p2.__str__()
# p3=Pupils("Петро",162)
# p3.__str__()
# print(p1.count,"участника змагань")
# #print(p1.__bool__())
# print(bool(p2))
# #print(p1.__len__())
# print(len(p3))

#Симулятор студента
import random as r
class Student:
    def __init__(self,name):
        self.name=name
        self.happy=r.randint(10,100)
        self.progress=r.randint(0,10)
        self.alive=True
    def study(self):
        print('Час для навчання')
        self.happy=r.randint(1,50)
        self.progress+=r.randint(1,10)
    def sleep(self):
        print('Час для cну')
        self.happy = r.randint(1, 10)
    def chill(self):
        print('Час для відпочинку')
        self.happy = r.randint(50, 100)
        self.progress += r.randint(5, 10)
    def isAlive(self):
        if 1<self.progress<5:
            print('тебе відчислять, вчись')
            self.alive=False
        elif self.progress <=1:
            print('Відчислять з інституту')
            self.alive = False
        elif self.progress >=5:
            print('Добре навчаешься!')
            self.alive = False
        def everyday(self):
            print("Рівень Щастя", self.happy)
            print("Прогрес навчання", self.progress)
        def studyLife(self,day):
            day="День №"+str(day)
            print(day)
            res=r.randint(1,3)
            if res==1:
                self.study()
            elif res==2:
                self.chill()
            else:
                self.sleep()
            self.everyday()
            self.isAlive()

st1=Student('Олег')
# print(st1.progress)
print("Життя студента",st1.name)
for k in range(1,8):
    if st1.alive==False:
        break
    st1.studyLife(k)