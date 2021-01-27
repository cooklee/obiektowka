class Product:
    next_id = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = self.get_next_id()

    @classmethod
    def get_next_id(cls):
        cls.next_id += 1
        return cls.next_id - 1

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class ShoppingCard:

    def __init__(self):
        self.products = {}
        self.quantities = {}

    def add_product(self, product):
        self.products[product.id] = product
        q = self.quantities.get(product.id, 0)
        self.quantities[product.id] = q + 1

    def remove_product(self, product):
        try:
            del self.products[product.id]
            del self.quantities[product.id]
        except KeyError:
            pass

    def change_product_quantity(self, product, new_quantity):
        if new_quantity < 0:
            raise ValueError
        if product.id in self.products:
            if new_quantity == 0:
                self.remove_product(product)
            else:
                self.quantities[product.id] = new_quantity

    def get_receipt(self):
        suma = 0
        s = ""
        for product in self.products.values():
            rabat = 1
            if self.quantities[product.id] >= 3:
                rabat = 0.7
            wartosc = self.quantities[product.id] * product.price * rabat
            s += f"{product.name} {self.quantities[product.id]} " \
                 f"{wartosc}\n"
            suma += wartosc
        s += f"całosc {suma}"
        return s



cebula = Product("cebula", 1.2)
jablko = Product("jablok", 2.2)
flaszka = Product("flaszka", 20)


sc = ShoppingCard()
sc.add_product(cebula)
sc.add_product(cebula)
sc.add_product(cebula)
sc.add_product(cebula)
sc.add_product(jablko)
sc.add_product(flaszka)
sc.add_product(flaszka)
sc.add_product(flaszka)
sc.add_product(flaszka)



print(sc.get_receipt())



