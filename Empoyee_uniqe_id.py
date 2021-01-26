import random


class Employee:
    next_id = 1

    def __init__(self, first_name, last_name):
        self.id = Employee.next_id
        Employee.next_id += 1
        self.first_name = first_name
        self.last_name = last_name
        self._salary = None
        self.__prawdziwe_imie = 'czesław'

    def set_salary(self, amount):
        if not (isinstance(amount, (int, float)) and amount > 0):
            raise ValueError("nie Poprawna wartość pensji")
        self._salary = amount


class Employee2:
    next_id = 1

    @classmethod
    def get_next_id(cls):
        id = cls.next_id
        cls.next_id += 1
        return id

    def __init__(self, first_name, last_name):
        self.id = self.get_next_id()
        self.first_name = first_name
        self.last_name = last_name
        self._salary = None
        self.__prawdziwe_imie = 'czesław'

    def set_salary(self, amount):
        if not (isinstance(amount, (int, float)) and amount > 0):
            raise ValueError("nie Poprawna wartość pensji")
        self._salary = amount


class SuperEmployee(Employee2):
    next_id = 1


for x in range(20):
    if random.randint(0, 1):
        a = Employee2(1, 1)
        a.get_next_id()
        print(a.id, 'Employee')
    else:
        b = SuperEmployee(1, 1)
        b.get_next_id()
        print(b.id, 'SuperEmployee')
