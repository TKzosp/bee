a, b = input().split()
a, b = int(a), int(b)

c = a *b
if c % b == 0 and c % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
