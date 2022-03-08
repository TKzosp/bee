s = float(input())
aumento = 0
def saida(aumento, s, per):
    aumento = s + (s * per)
    print(f'Novo salario: {aumento:.2f}')
    print(f'Reajuste ganho: {s * per:.2f}')
    print(f'Em percentual: {per*100:.0f} %')
if s <= 400:
    per = 0.15
    saida(aumento, s, per)
elif s > 400 and s <= 800:
    per = 0.12
    saida(aumento, s, per)
elif s > 800 and s<= 1200:
    per = 0.10
    saida(aumento, s, per)
elif s > 1200 and s<= 2000:
    per = 0.07
    saida(aumento, s, per)
else:
    per = 0.04
    saida(aumento, s, per)
