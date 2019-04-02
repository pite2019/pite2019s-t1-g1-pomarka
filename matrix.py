import math
from copy import deepcopy


class Matrix:
    def __init__(self, *args, **kwargs):
        N = math.sqrt(len(args))
        if math.floor(N) != N:
            raise ValueError("wrong number of arguments")
        self.N = int(N)
        self.matrix = [[] for x in range(self.N)]
        for i, x in enumerate(args):
            self.matrix[i // self.N].append(x)

    def __str__(self):
        result = "["
        flattened = [x for y in self.matrix for x in y]
        longest_num_chars = len(str(max(flattened)))
        for i, row in enumerate(self.matrix):
            for j, column in enumerate(row):
                if j == 0 and i > 0: # wyrównanie przed pierwsza kolumną
                    result += " "
                result += str(column)
                if j != (len(row)-1):
                    result += ", "
                    result += " " * (longest_num_chars - len(str(column))) # wyrównanie większych liczb
                elif i != (len(self.matrix)-1): # newline po każdym N elementów
                    result += "\n"

        result += "]"
        return result

    def __copy__(self):
        m = Matrix()
        m.N = self.N
        m.matrix = deepcopy(self.matrix)
        return m

    def __iadd__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if other.N != self.N:
                raise ValueError("matrices with different dimensions")

        for i in range(self.N):
                for j in range(self.N):
                    self.matrix[i][j] += other.matrix[i][j]

        return self

    def __isub__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if other.N != self.N:
                raise ValueError("matrices with different dimensions")

        for i in range(self.N):
                for j in range(self.N):
                    self.matrix[i][j] -= other.matrix[i][j]

        return self

    def __radd__(self, i):
        return self + i

    def __add__(self, other):
        if isinstance(self, Matrix) and isinstance(other, Matrix):
            if other.N != self.N:
                raise ValueError("matrices with different dimensions")
            m = self.__copy__()

            for i in range(self.N):
                for j in range(self.N):
                    m.matrix[i][j] += other.matrix[i][j]

            return m

        if isinstance(self, Matrix) and isinstance(other, int):
            m = self.__copy__()

            for i in range(self.N):
                for j in range(self.N):
                    m.matrix[i][j] += other

            return m

    def __sub__(self, other):
        if other.N != self.N:
            raise ValueError("matrices with different dimensions")
        m = self.__copy__()

        for i in range(self.N):
            for j in range(self.N):
                m.matrix[i][j] -= other.matrix[i][j]

        return m

    def __matmul__(self, other):
       if other.N != self.N:
            raise ValueError("matrices with different dimensions")
       tmp_list = []
       s = 0

       for x in range(self.N):
           for y in range(self.N):
               for k in range(self.N):
                   s += self.matrix[x][k] * other.matrix[k][y]
               tmp_list.append(s)
               s = 0

       return Matrix(*tmp_list)