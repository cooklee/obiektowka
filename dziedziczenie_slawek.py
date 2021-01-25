class Car:

    def __init__(self, marka, model, silnik):
        self.brand = marka
        self.model = model
        self.engine = silnik

    def __str__(self):
        return f"{self.brand} {self.model} {self.engine}"


class Truck(Car):
    def __init__(self, marka, model, silnik, ladownosc):
        super().__init__(marka, model,silnik)
        self.capacity = ladownosc



    def __str__(self):
        s = super().__str__()
        return  s + " To jest super ciężarówka"

class SuperTruck(Truck):
    def __str__(self):
        s = super(Car, self).__str__()
        return s + " To jest super Super Cieżarówka"

t= Truck("Star", 'V11', 'Disel', 1)
t1= Truck("Star", 'V12', 'Disel', 2)
t2= Truck("Star", 'V13', 'Disel', 3)

print(t.__init__('a','b','d', 1))
print(t)
print(t1)
print(t2)



