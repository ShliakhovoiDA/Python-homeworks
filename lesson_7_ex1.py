class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix) + '\n'

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for i_2 in range(len(other.matrix[i])):
                self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
        return Matrix.__str__(self)


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
