import time
import itertools


class TrafficLight:
    __color = [["RED", [7, 31]], ["YELLOW", [2, 33]], ["GREEN", [7, 32]], ["YELLOW", [2, 33]]]

    # class cycle(object):
    #     """ Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely. """

    #     def __init__(self, *args, **kwargs):  # real signature unknown
    #         pass

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[7m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])


let_the_color_be = TrafficLight()
let_the_color_be.running()
