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
        # print(cls.__name__,)
        # print(f"cls==Employee2-> {cls == Employee2}")
        # print(f"cls==SuperEmployee-> {cls == SuperEmployee}")
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
    pass

import random
for x in range(20):
    if random.randint(0,1):
        a = Employee2(1,1)
        print(a.id, 'Employee')
    else:
        a = SuperEmployee(1,1)
        print(a.id, 'SuperEmployee')
