class Rectangle:
  def __init__(self, width, height, co):
    self.__width = width
    self.__height = height
    self.__co = co
  def perimeter(self):
    return (self.__width + self.__height) * 2
  def area(self):
    return self.__width * self.__height
  def color(self):
    return self.__co.title()

arr = input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
  r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
  print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else: print('INVALID')