class LightSabres:

    types = {'blue':'light', 'green':'light', 'red':'dark'}
    power = 20

    def __init__(self, color):
        if color in LightSabres.types:
            self._color = color


a = LightSabres('red')
b = LightSabres('green')
c = LightSabres('blue')
for item in dir(a):
    print(item)
print(a.types, b.types,c.types, sep="\n")
a.types= {
    1,2,3
}
print(a.types, b.types,c.types, sep="\n")
a.power = 115
print(a.power, b.power, c.power)

