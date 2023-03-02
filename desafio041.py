n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
print('Os numeros pares entre {} e {}'.format(n1, n2))
for c in range(n1, n2+1, 2):
    print(c)
print('FIM')