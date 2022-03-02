a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

# A)
tr = (a * c) / 2

# B)
ac = 3.14159 * c**2

# C)
atra = ((a + b) * c) / 2

# D)
aqua = b*b

# E)
aret = a * b

print(f'TRIANGULO: {tr:.3f}\nCIRCULO: {ac:.3f}\nTRAPEZIO: {atra:.3f}\nQUADRADO: {aqua:.3f}\nRETANGULO: {aret:.3f}')