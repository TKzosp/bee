a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)

if a % 2 == 0:
    aposi = True
else:
    False

if b > c and d > a and (c+d) > (b+a) and c > 0 and d > 0 and aposi == True:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')