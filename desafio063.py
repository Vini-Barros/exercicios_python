total = cont = menor = cont1 = 0
barato = ''
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont1 += 1
    total += preco
    if preco >= 1000:
        cont += 1
    if cont1 == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?[S/N]'))
    if resp == 'N':
        break
print(f'O total da compra foi de {total:.2} reais')
print(f'Você comprou {cont} produtos acima de 1000 reais')
print(f'O produto mais barato custa {menor} e se chama {barato}')