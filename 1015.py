from math import sqrt
x, y = input().split()
x2 , y2 = input().split()
x, y, x2, y2 = float(x), float(y), float(x2), float(y2)
dis = sqrt((x2 - x)**2 + (y2 - y)**2)
print(f'{dis:.4f}')