from datetime import datetime

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def create_person(cls, name, year_of_birth):
        age = datetime.now().year - year_of_birth
        return cls(name, age)

p = Person("Slawek", 37)
k1 = Person.create_person("Slawek", 1984)
print(p.name, p.age)
print(k1.name, k1.age)
print(k1.__class__.__name__)
