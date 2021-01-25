class Calculator:

    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        wynik = num1 + num2
        text = f"add {num1} + {num2} got {wynik}"
        self.history.append(text)
        return wynik

    def multiplay(self, num1, num2):
        wynik = num1 * num2
        text = f"add {num1} * {num2} got {wynik}"
        self.history.append(text)
        return wynik

    def silnia(self, num1):
        wynik = 1
        for x in range(1,num1+1):
            wynik *= x
        text = f"{num1}! got {wynik}"
        self.history.append(text)
        return wynik


    def print_operations(self):
        for item in self.history:
            print(item)

c = Calculator()
print(c.add(1, 2))
print(c.multiplay(1, 2))
print(c.silnia(5))
print(c.add(1, 3))
print(c.add(1, 4))
print(c.add(1, 5))



