import operator
from functools import reduce

class operable(object):
    def __add__(self,other):
        if isinstance(other, operable):
            d = calculation()
            d.operator = operator.__add__
            d.operands = [self,other]
            return d

    def __mul__(self,other):
        if isinstance(other,operable):
            d = calculation()
            d.operator = operator.__mul__
            d.operands = [self,other]
            return d

class calculation(operable):
    def __init__(self):
        self.operands = []
        self.operator = None

    @property
    def value(self):
        return reduce(self.operator, [x.value for x in self.operands])

    @property
    def calculation(self):
        return (" %s " % str(self.operator)).join([x.__repr__() for x in self.operands])

    def __repr__(self):
        return "%d [ %s ] " % ( self.value, self.calculation )

class constant(operable):
    def __init__(self, x = 0):
        self._value = x

    def __repr__(self):
        return "%d" %( self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,new_val):
        self._value = new_val


def test_1():
    a = constant(2)
    b = constant(3)

    c = a + b
    d = a * b

    z = a + b + c + d

    print ("c is",c)
    print ("d is",d)
    print ("z is ",z)

    b.value = 5

    print ("c is now",c)
    print ("d is now",d)
    print ("z is now ",z)



if __name__ == "__main__":
    test_1()