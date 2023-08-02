from math import factorial
from Exceptions import FactorialException, TypeException, MyStopIteration


class Factorial:
    def __init__(self, start, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if not isinstance(start, int):
            raise TypeException(start)
        if stop is not None and not isinstance(stop, int):
            raise TypeException(stop)
        if not isinstance(step, int):
            raise TypeException(step)
        if self.stop is None and self.start > 0:
            self.stop = self.start
            self.start = 1
        else:
            raise FactorialException(self.start)

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            res = factorial(self.start)
            self.start += self.step
            return res
        raise MyStopIteration(self.stop)


if __name__ == '__main__':
    f = Factorial(10.20)
    # f = Factorial('ten')
    # f = Factorial(10)
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())