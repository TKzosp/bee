while True:
    M, N  = input().split()
    M , N = int(M), int(N)
    c = M + N
    c = str(c)
    c = c.replace('0', '')
    if M == 0 and N == 0:
        break
    else:
        print(f'{c}')