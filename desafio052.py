from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
print('''Escolha oque você quer fazer com os numeros
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] EXIT''')
jogador = int(input('Faça sua escolha: '))
if jogador == 1:
    soma = n1 + n2
    print('A soma dos numeros {} e {} vale {}'.format(n1, n2, soma))
elif jogador == 2:
    multiplicar = n1 * n2
    print('O resultado da multiplicação entre {} e {} é {}'.format(n1, n2, multiplicar))
elif jogador == 3:
    lista = [n1, n2]
    print('O maior numero é {}'.format(max(lista)))
elif jogador == 4:
    novos = int(input('Se arrependeu desses numeros ? digite outros: '))