peca1, npeca, vpeca =  input().split()

peca2, npeca2, vpeca2 = input().split()

peca1 = int(peca1)
peca2 = int(peca2)
npeca = int(npeca)
npeca2 = int(npeca2)
vpeca = float(vpeca)
vpeca2 = float(vpeca2)


total = (npeca * vpeca) + (npeca2 * vpeca2)

print(f'VALOR A PAGAR: R$ {total:.2f}')