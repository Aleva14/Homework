class vector:
    def __init__(self, n = None, coord = None):
        if (n == None) and (coord == None):
            self.n = 2
            self.coord = [0, 0]
        elif n == None:
            self.n = len(coord)
            self.coord = coord
        elif coord == None:
            self.n = n
            self.coord = [0 for i in range(0, n)]            
    def __add__(self, v):
        if self.n != v.n:
            print 'Not defined'
        else:
            result = vector(self.n)
            for i in range(0, self.n):
                result.coord[i] = self.coord [i] + v.coord[i]
            return result
    def __sub__(self, v):
        if self.n != v.n:
            print 'Not defined'
        else:
            result = vector(self.n)
            for i in range(0, self.n):
                result.coord[i] = self.coord[i] + v.coord[i]
            return result
    def __mul__(self, v):
        if self.n != v.n:
            print 'Not defined'
        else:
            c = 0
            for i in range(0, self.n):
                c += self.coord[i] * v.coord[i]
            return c
    def dump(self):
        print(self.coord)

a = vector(coord = [1, 2, 3])
b = vector(coord = [1, 1, 1])
c = a * b
print c

