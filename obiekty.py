class BankAccount:

    def __init__(self, imie, nazwisko, nr_konta, stan):
        self.first_name = imie
        self.last_name = nazwisko
        self.number = nr_konta
        self.cash = stan

    def wypisz(self):
        s = f"""
        imie:{self.first_name}
        nazwisko:{self.last_name}
        nr:{self.number}
        stan:{self.cash}
            """
        print(s)

def wypisz(account):
    s = f"""
            imie:{account.first_name}
            nazwisko:{account.last_name}
            nr:{account.number}
            stan:{account.cash}
                """
    print(s)

b = BankAccount(nazwisko="Bogusławski", nr_konta=123, stan=0, imie="Sławek")
b1 = BankAccount('Gosia', 'Samosia', 1, 1000)
b.wypisz() # wypisz(b)
b1.wypisz() # wypisz(b1)

c = BankAccount('Celina', 'Henka', 2, -500)
c1 = BankAccount("Agnieszka", 'Gamon', 3, 2000)
