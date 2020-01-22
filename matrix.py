from random import randrange


class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def __info__(self):
        return self.matrix

    def __str__(self):
        return f'Size : [{self.n};{self.m}]. Matrix : {self.matrix}'

    def fill(self, randomize=False, manually=False):
        if randomize:
            for i in range(self.n):
                for j in range(self.m):
                    self.matrix[i][j] = randrange(10)
            return self.matrix
        else:
            for i in range(self.n):
                for j in range(self.m):
                    self.matrix[i][j] = int(input(f'input [{i},{j}]: '))
            return self.matrix

    def transpose(self):
        try:
            for i in range(1, self.n):
                for j in range(i):
                    self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
            return self.matrix
        except IndexError:
            print("Sry i only know how to transpose square matrix")

    def get_row(self, row):
        return self.matrix[row]

    def get_col(self, col):
        return [x[col] for x in self.matrix]

    def get_main_diagonal(self):
        if self.is_square(self):
            return [self.matrix[i][i] for i in range(self.n)]
        else:
            raise ValueError('Only square matrix have diagonal')

    def is_diagonal(self):
        if not all(self.get_main_diagonal(self)):
            return False
        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] == 0 and self.matrix[i][j] is not self.matrix[i][i]:
                    return False
        return True

    def is_square(self):
        return self.n == self.m

    def shape(self):
        return self.matrix[0][0], self.matrix[0][self.m - 1], \
               self.matrix[self.n - 1][0], self.matrix[self.n - 1][self.m - 1]

    def is_zero(self):
        for i in range(self.n):
            for j in range(self.m):
                if not self.matrix[i][j] == 0:
                    return False
        return True

    def __add__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise ValueError("The operand must be Matrix class instance")
        if not self.m == other_matrix.m or not self.n == other_matrix.n:
            raise ValueError("Matrix must be equal size")
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] += other_matrix.matrix[i][j]
        return self.matrix

    def __sub__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise ValueError("The operand must be Matrix class instance")
        if not self.m == other_matrix.m or not self.n == other_matrix.n:
            raise ValueError("Matrix must be equal size")
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] -= other_matrix.matrix[i][j]
        return self.matrix

    def __mul__(self, item):
        if isinstance(item, int):
            for i in range(self.n):
                for j in range(self.m):
                    self.matrix[i][j] *= item
        elif isinstance(item, Matrix):
            for i in range(self.n):
                for j in range(self.m):
                    self.matrix[i][j] *= item.matrix[i][j]
        else:
            raise ValueError("You can add only Matrix to integer or Matrix to Matrix")
        return self.matrix


if __name__ == '__main__':
    m = Matrix(3, 3)
    k = Matrix(3, 3)
    print(k.fill(manually=True))
    print(m.fill(randomize=True))
    # print(m.get_main_diagonal())
    # print(m.is_diagonal([1, 5, 9]))
    # print(m.shape())
    # print(m * k)
    # print(m.is_zero())
    # print(k + m)
    # print(m.transpose())
    # print(k - m)
    print(k.is_diagonal())
