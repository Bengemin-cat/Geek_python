from time import sleep
import colorama


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        while True:
            for i in range(len(self.__color)):
                print(f'\rСейчас горит {self.__color[i]}',end='')
                if self.__color[i] == 'red':
                    sleep(7)
                elif self.__color[i] == 'yellow':
                    sleep(2)
                elif self.__color[i] == 'green':
                    sleep(5)


traffic = TrafficLight()

traffic.running()
