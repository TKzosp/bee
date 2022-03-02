a, b, c, d  = input().split()
a, b, c, d = float(a), float(b), float(c), float(d)
media = ((a * 2) + (b * 3) + (c * 4) + (d * 1)) / 10
if media < 5.0:
    print(f'Media: {media:.1f}')
    print(f'Aluno reprovado.')
elif media >= 5.0 and media <7:
    print(f'Media: {media:.1f}')
    print(f'Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media_final = (media + exame) / 2
    if media_final < 5.0:
        print(f'Aluno reprovado.')
        print(f'Media: {media_final:.1f}')
    elif media_final >= 5.0:
        print(f'Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
else:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')