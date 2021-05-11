from time import sleep

class TrafficLight:
    def _light_start(self):
        while TrafficLight:
            print("Горит красный сигнал!")
            sleep(7)
            print("Горит желтый сигнал!")
            sleep(2)
            print("горит зеленый сигнал")
            sleep(7)
            break

count = TrafficLight()
count._light_start()




