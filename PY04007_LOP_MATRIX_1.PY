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
    return Matrix(self.row, self.row, res)
  def __str__(self):
    for i in self.matrix:
      print(*i)
    return ''

for case in range(int(input())):
  r, c = [int(i) for i in input().split()]
  matrix = []
  for i in range(r):
    matrix += [[int(i) for i in input().split()]]
  print(Matrix(r, c, matrix).mul())