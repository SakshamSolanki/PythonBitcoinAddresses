P = 2 ** 256 - 2 ** 32 - 977

class FieldElement:

    def __init__(self, num , prime):
        if num >= prime or num < 0:
            error = 'Num {} not in fueld range 0 to {}'.format(num , prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FinitElement_{})({})'.format(self.prime, self.num)

    def __eq__(self , other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self , other):
        if other is None:
            return False
        return not (self == other)

    def __add__(self , other):
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        return self.__class__(num , self.prime)

    def __sub__(self , other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num , self.prime)

    def __mul__(self , other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num , self.prime)

    def __pow__(self , exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num , n , self.prime)
        return self.__class__(num , self.prime)

    def __truediv__(self , other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        other_inv = pow(other.num , self.prime - 2 , self.prime)
        num = self.num * other_inv % self.prime
        return self.__class__(num , self.prime)
    
    def __rmul__(self , coef):
        num = (self.num * coef) % self.prime
        return self.__class__(num , self.prime)


class S256Field(FieldElement):

    def __init__(self , num , prime = None):
        super().__init__(num , prime = P)

    def __repr__(self):
        return '{:x}'.format(self.num).zfill(64)
