N = int(input())
ano = N // 365
N = N - ano * 365 
mes = N // 30
N = N - mes * 30
dia = N
print(f'{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)')

