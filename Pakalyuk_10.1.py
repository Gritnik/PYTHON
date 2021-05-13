class Matrix:


    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(map(lambda r: ' '.join(map(str, r)), self.matrix)) + '\n'

    def __add__(self, other):
        return Matrix(map(lambda r_1, r_2: map(lambda x, y: x + y, r_1, r_2), self.matrix, other.matrix))


num_1 = Matrix([[31, 22], [37, 43], [51, 86]])
num_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
num_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
num_4 = Matrix([input("первый набор цифр: "), input("второй набор цифр: ")])

print(num_1)
print(num_2)
print(num_3)
print(num_4)