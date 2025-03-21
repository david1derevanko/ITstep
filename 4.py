class Employee:
    def __init__(self, name, position, salary):

        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):

        return f"Заробітна плата {self.name}: {self.salary} грн"



employee1 = Employee("Іван Петренко", "Менеджер", 25000)
employee2 = Employee("Марія Коваль", "Бухгалтер", 30000)

print(employee1.get_salary_info())
print(employee2.get_salary_info())