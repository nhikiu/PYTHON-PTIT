class Matrix:
  def __init__(self, row, column, matrix):
    self.row = row
    self.column = column
    self.matrix = matrix
  def mul(self):
    res = []
    for i in range(self.row):
      res += [[0] * self.row]
    for i in range(self.row):
      for j in range(self.row):
        for k in range(self.column):
          res[i][j] += self.matrix[i][k] * self.matrix[j][k]
    return Matrix(self.row, self.column, res)
  def __str__(self):
    for i in self.matrix:
      print(*i)
    return ''

for case in range(int(input())):
  n, m = [int(i) for i in input().split()]
  ip = []
  for i in range(n):
    ip.append([int(j) for j in input().split()])
  matrix = Matrix(n, m, ip)
  print(matrix.mul())