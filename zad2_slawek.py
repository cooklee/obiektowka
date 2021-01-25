class Shape:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def describe(self):
        print(self)

    def distance(self, shape):
        a = (self.x - shape.x)**2
        b = (self.y - shape.y) ** 2
        return (a+b)**0.5

    def __str__(self):
        return  f"kształt w o środku w punkcie {self.x, self.y} i kolorze {self.color}"


a = Shape(0,0,"red")
b = Shape(1,1, "blue")

print(a.distance(b))
print(b.distance(a))
b.describe()