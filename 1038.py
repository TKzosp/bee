escolha, quantidade = input().split()
escolha, quantidade = int(escolha), int(quantidade)
if escolha == 1:
    total = quantidade * 4.00
elif escolha ==2:
     total = quantidade * 4.50
elif escolha ==3:
    total = quantidade * 5.00
elif escolha ==4:
    total = quantidade * 2.00
else:
    total = quantidade * 1.50

print(f'Total: R$ {total:.2f}')