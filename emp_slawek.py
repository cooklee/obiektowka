class Employee:

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name =first_name
        self.last_name = last_name
        self._salary = None
        self.__prawdziwe_imie = 'czesław'

    def set_salary(self, amount):
        if not (isinstance(amount, (int, float)) and amount > 0):
            raise ValueError("nie Poprawna wartość pensji")
        self._salary = amount


