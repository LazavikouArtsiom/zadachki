from random import randrange


class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

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

    def __info__(self):
        return self.matrix

    def transpose(self):
        for i in range(1, self.n):
            for j in range(i):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

    def get_row(self, row):
        return self.matrix[row]

    def get_col(self, col):
        return [x[col] for x in self.matrix]

    def get_main_diagonal(self):
        if Matrix.is_square(self):
            return [self.matrix[i][i] for i in range(self.n)]
        else:
            raise ValueError('Only square matrix have diagonal')

    def is_diagonal(self, ls):
        return ls == Matrix.get_main_diagonal(self)

    def is_square(self):
        return self.n == self.m

    def shape(self):
        return self.matrix[0][0], self.matrix[0][self.m - 1], \
               self.matrix[self.n - 1][0], self.matrix[self.n - 1][self.m - 1]

    def __add__(self, other_matrix):
        pass

    def __sub__(self, other_matrix):
        pass

    def __mul__(self, integer):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] *= integer
        return self.matrix


if __name__ == '__main__':
    from copy import copy

    m = Matrix(3, 3)
    k = Matrix(3, 3)
    print(k.fill(randomize=True))
    print(m.fill(randomize=True))
    # print(m.get_main_diagonal())
    # print(m.is_diagonal([1, 5, 9]))
    # print(m.shape())
    # print(m * 2)

