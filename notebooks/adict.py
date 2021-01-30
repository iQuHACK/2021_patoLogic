from collections import defaultdict

class adict(defaultdict):
    """Dictionary with algebraic operations"""
    def __add__(self, other):
        new = adict(int)
        for k in self.keys() | other.keys():
            new[k] = self[k] + other[k]
        return new

    def __sub__(self, other):
        new = adict(int)
        for k in self.keys() | other.keys():
            new[k] = self[k] - other[k]
        return new

    def __mul__(self, other):
        new = adict(int)
        if isinstance(other, int):
            for k, v in self.items():
                new[k] = v * other
            return new
        else:
            for k in self.keys() | other.keys():
                new[k] = self[k] * other[k]
            return new

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        new = adict(int)
        for k in self.keys() | other.keys():
            new[k] = self[k] / other[k]
        return new