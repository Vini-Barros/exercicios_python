from random import randint
vitorias = 0
print('=-'*30)
print('JOGO DO PAR OU IMPAR')
print('=-'*30)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar [P/I] ? '))
    print(f'Você jogou {jogador} e o computador escolheu {computador} o total disso foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('FOI PAR')
            print('\033[34mVOCÊ GANHOU\033[m')
            vitorias += 1
        else:
            print('FOI IMPAR')
            print('\033[31mVOCÊ PERDEU\033[m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('FOI IMPAR')
            print('\033[34mVOCÊ VENCEU!\033[m')
            vitorias += 1
        else:
            print('FOI PAR')
            print('\033[31mVOCÊ PERDEU\033[m')
            break
    print('Vamos jogar novamente...')
    print('\033[36m=-\033[m'* 20)
print(f'GAME OVER, você venceu {vitorias} vezes')