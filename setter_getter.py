import uuid


class Employee:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = None
        self.__uuid = uuid.uuid4()

    def set_salary(self, amount):
        if not (isinstance(amount, (int, float)) and amount > 0):
            raise ValueError("nie Poprawna wartość pensji")
        self._salary = amount

    def get_uuid(self):
        return self.__uuid


e = Employee(1, 'Sławomir', 'Bogusławski')



class Sonda:

    def __init__(self, distance):
        self.set_distance(distance)

    def set_distance(self, distance):
        self._distance = distance / 4

    def get_distance(self):
        return self._distance * 4

class Sonda2:

    def __init__(self, distance):
        self.distance = distance

    @property
    def distance(self):
        return self._distance * 4

    @distance.setter
    def distance(self, distance):
        self._distance = distance / 4


s = Sonda(1000)
s.set_distance(40)
print(s._distance)
print(s.get_distance())


s2 = Sonda2(1000)
s2.distance = 40
print(s2._distance)
print(s2.distance)

