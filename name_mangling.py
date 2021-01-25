class User:

    def __init__(self):
        self.__name = "ala ma kota"


    def print(self):
        print(self.__name)

class SUser(User):
    pass

    def suser_print(self):
        print(self._User__name)


u =  User()
u.print()

s = SUser()
s.print()
s.suser_print()