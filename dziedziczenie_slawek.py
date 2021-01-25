class Car:

    def __init__(self, marka, model, silnik):
        self.brand = marka
        self.model = model
        self.engine = silnik

    def __str__(self):
        return f"{self.brand} {self.model} {self.engine}"


class Truck(Car):
    def __str__(self):
        s = super().__str__()
        return  s + " To jest super ciężarówka"

class SuperTruck(Truck):
    def __str__(self):
        s = super(Car, self).__str__()
        return s + " To jest super Super Cieżarówka"

t= Truck("Star", 'V11', 'Disel')
t1= Truck("Star", 'V12', 'Disel')
t2= Truck("Star", 'V13', 'Disel')
st3 = SuperTruck("Super Truck", 'V23', 'Electric')

print(t)
print(t1)
print(t2)
print(st3)


