# Iterate over an Object's attributes in Python

class Employee():
    cls_id = 'employee'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee('bobbyhadz', 100)

for attribute, value in emp1.__dict__.items():
    # name bobbyhadz
    # salary 100
    print(attribute, value)