listaum = []
maior = menor = 0
for c in range(0, 5):
    listaum.append(int(input('digite um valor: ')))
    if c == 0:
        maior = menor = listaum[c]
    else:
        if listaum[c] > maior:
            maior = listaum[c]
        if listaum[c] < menor:
            menor = listaum[c]
print('-='*30)

print(f'Você digitou os valores {listaum}')
print(f'O maior valor é {maior} e esta na posição', end='')
for i, v in enumerate(listaum):
    if v == maior:
        print(f' {i}...')
print(f'O menor valor é {menor} e esta na posição', end='')
for i, v in enumerate(listaum):
    if v == menor:
        print(f' {i}...')
print('-='*30)