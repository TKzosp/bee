a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

mab = (a + b + abs(a-b)) / 2
if c < mab:
    mabc = mab
else:
    mabc = c
print(f'{mabc} eh o maior')