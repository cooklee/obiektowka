class BankAccount:

    def __init__(self, imie, nazwisko, nr_konta, stan):
        self.first_name = imie
        self.last_name = nazwisko
        self.number = nr_konta
        self.cash = stan

class Skowronek:

    def __init__(self, imie, nazwisko, nr_konta, stan):
        self.first_name = imie
        self.last_name = nazwisko
        self.number = nr_konta
        self.cash = stan


b = BankAccount(nazwisko="Bogusławski", nr_konta=123, stan=0, imie="Sławek")
b1 = BankAccount('Gosia', 'Samosia', 1, 1000)
c = BankAccount('Celina', 'Henka', 2, -500)
c1 = BankAccount("Agnieszka", 'Gamon', 3, 2000)
s = Skowronek("Skowronek", 'Malutki', 4, 100)
lst = [b, b1, c, c1, s]


def wypisz(dupa):
    s = f"""
imie:{dupa.first_name}
nazwisko:{dupa.last_name}
nr:{dupa.number}
stan:{dupa.cash}
    """
    print(s)

for item in lst:
    wypisz(item)
    print("_____________________________")
