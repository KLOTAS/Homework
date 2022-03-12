from abc import ABC , abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum_consumption(self, list_soits):
       a = 0
       for suit in list_soits:
           a += suit.consumption
       return a


coat = Coat(30)
costume = Suit(2.78)
costume_2 = Suit(3.14)
costume_3 = Suit(1.26)
costume_4 = Suit(2.10)
list_costumes = [costume_4, costume_3, costume_2, costume]
print(coat.consumption)
print(costume.consumption)
print(costume.sum_consumption(list_costumes))
