listagem = ('Lapis', 1.75,
            'Borracha', 2,
            'Caderno', 15,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 10,
            'Mochila', 120.0,
            'caneta', 1.50,
            'Livro', 35.50)
print('-' * 40)
print('Listagem de preço')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
