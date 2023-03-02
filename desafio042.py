soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        print(c)
print('A soma vale {}'.format(soma))