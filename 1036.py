a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

delta = (b ** 2) - 4 * a * c


if a == 0 or delta < 0:
    print('Impossivel calcular')
# elif delta < 0:
#     print('Impossivel calcular')
else:
    r1 = (-b + delta ** (1 / 2)) / (2 * a)
    r2 = (-b - delta ** (1 / 2)) / (2 * a)
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')