n = float(input())

if n < 0 or n > 100:
    print('Fora de intervalo')
elif n > 25 and n <= 50:
    if n > 25:
        print(f'Intervalo (25,50]')
elif n > 50 and n <= 75:
    print(f'Intervalo (50,75]')
elif n > 75 and n<= 100:
    print(f'Intervalo (75,100]')
else:
    print(f'Intervalo [0,25]')