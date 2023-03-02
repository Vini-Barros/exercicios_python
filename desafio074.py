numeros = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Numero adicionado...')
    else:
        print('Numero não adicionado...')
    pessoa = str(input('Quer continuar ?[S/N]'))
    if pessoa in 'N':
        break
print('=='*25)
numeros.sort()
print(f'Você digitou os valores {numeros}')