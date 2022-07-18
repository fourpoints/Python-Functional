from functools import reduce
from collections import deque


class Functional:
    # numpy compatibility
    # numpy overrides __rXXX__ functions otherwise
    __array_ufunc__ = None
    __array_priority__ = 0


class Map(Functional):
    def __init__(self, map):
        self.map = map
    def __ror__(self, other):
        return map(self.map, other)


class Filter(Functional):
    def __init__(self, filter):
        self.filter = filter
    def __ror__(self, other):
        return filter(self.filter, other)


class Reduce(Functional):
    def __init__(self, reduce, initial=None):
        self.reduce = reduce
        self.initial = initial
    def __ror__(self, other):
        return reduce(self.reduce, other, self.initial)


class Apply(Functional):
    def __init__(self, function):
        self.function = function
    def __ror__(self, other):
        return self.function(other)


class Print(Functional):
    def __ror__(self, other):
        print(other)
        return other


class Chain(Functional):
    def __init__(self, *functions):
        self.functions = functions
    @staticmethod
    def _apply(x, f):
        return f(x)
    def __ror__(self, other):
        return reduce(self._apply, self.functions, other)


class Zip(Functional):
    # Often equivalent to transposition
    def __ror__(self, other):
        return zip(*other)


class Eval(Functional):
    def __ror__(self, other):
        deque(other, maxlen=0)


class Print(Functional):
    def __ror__(self, other):


class Get(type):
    def __getitem__(cls, key):
        return Get(key)


class Get(Functional, metaclass=Get):
    def __init__(self, key):
        self.key = key
    def __ror__(self, other):
        return other[self.key]


class Attr(type):
    def __getattribute__(cls, attribute):
        return Attr(attribute)


class Attr(Functional, metaclass=Attr):
    def __init__(self, attribute):
        self.attribute = attribute
    def __ror__(self, other):
        return getattr(other, self.attribute)
