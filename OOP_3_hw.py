from random import gauss

class CustomFloat:  # родительский
    def __int__(self):
        return int(float(self))

    def __add__(self, other):
        if isinstance(other, CustomFloat):
            other = float(other)
        elif not isinstance(other,(float, int)):
            raise TypeError
        return float(self) + other

    def __radd__(self, other):
        return self + other

    # перегрузка операторов сравнения
    def __eq__(self, other):  # ==
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) == other


    def __lt__(self, other): # <
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) < other

    def __ge__(self, other): # >=
        return not self.__lt__(other)

    def __gt__(self, other):  # >
        if isinstance(other, RandomFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            raise TypeError
        return float(self) > other

    def __le__(self, other):  # <=
        return not self.__gt__(other)

    # def checktype(self, other):
    #     if not isinstance(other, (int, float, CustomFloat)):
    #         raise TypeError
    #     if isinstance(other, CustomFloat):
    #         return float(other)
    #     return other

class RandomFloat(CustomFloat):  # дочерний
    def __init__(self,mu: float, /, *, sigma: float = 1.):
        if not isinstance(mu, float) or not isinstance(sigma, float):
            raise TypeError
        self.mu = mu
        self.sigma = sigma

    def __float__(self):
        return gauss(self.mu, self.sigma)


class EpsilonFloat(CustomFloat):
    def __init__(self, /, data, *, epsilon=1e-5):
        if isinstance(data, float) and isinstance(epsilon, float):
            if epsilon >= 0:
                self.data = data
                self.epsilon = epsilon
            else:
                raise ValueError
        else:
            raise TypeError

    def __float__(self):
        return self.data

    def __eq__(self, other):  # ==
        if isinstance(other, EpsilonFloat):
            other = float(other)
        elif not isinstance(other, (float, int)):
            return False
        return abs(float(self.data) - other) < self.epsilon

    def __ne__(self, other): # !=
        return not self.__eq__(other)

    def __lt__(self, other):  # <
        if not isinstance(other, (float, int, EpsilonFloat)):
            raise TypeError
        if isinstance(other, EpsilonFloat):
            return float(self)
        return float(self) - other < -self.epsilon

    def __gt__(self, other):  # >
        if not isinstance(other, (float, int, EpsilonFloat)):
            raise TypeError
        if isinstance(other, EpsilonFloat):
            return float(self)
        return float(self) - other > self.epsilon

    def __ge__(self, other):  # >=
        return not self.__lt__(other)

    def __le__(self, other):  # <=
        return not self.__gt__(other)

c = EpsilonFloat(12.00000123456)
d = EpsilonFloat(10.00000123488)
# c != d
# c > d
# c < d
# c >= d
# c <= d
c == d
