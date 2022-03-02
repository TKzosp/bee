N = int(input())
hora = N // 60**2
N = N - hora * 60**2
mim = N // 60
N = N - mim*60
seg = N

print(f'{hora}:{mim}:{seg}')