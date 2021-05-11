class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    #длинна 5000
    #ширина 20м
    def road_profile(self):
        return format(((self._length * self._width * 25 * 5) / 1000), '.0f')


width = 20
length = 5000
road_1 = Road(5000, 20)
print(road_1.road_profile(), 'тонн асфальта необходимо для данной дороги')
# использовать формулу: длина * ширина * масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т