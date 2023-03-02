num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um valor: '))
    cont = cont + 1
    soma = soma + num
    print('\033[36m{}\033[m'.format(soma))
print('Você digitou {} numeros e asoma entre eles é {}'.format(cont - 1, soma - 999))
print('FIM')