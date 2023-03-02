numero = (int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')))
print(f'Você digitou os numeros {numero}')
print(f'O numero 9 apareceu {numero.count(9)} vezes')
print(f'O numero 3 aparace pela primeira vez na posição {numero.index(3)}')
for n in numero:
    if n % 2 == 0:
        print(f'Os numeros pares são {n}')