from random import randint
from time import sleep
print('=-' * 30)

print('           JOKENPÔ               ')

print('=-' * 30)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Faça sua jogada: 
[1] Pedra
[2] Papel
[3] Tesoura''')

jogador = int(input('Qual a sua jogada ? '))

print('JO')

sleep(1)

print('KEN')

sleep(1)

print('PÔ')

sleep(1)

print('*' * 50)

print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu a opção {}'.format(jogador))

print('*' * 50)

if computador == 1:  # pedra
    if jogador == 1:  # pedra
        print('EMPATE')
    elif jogador == 2:  # papel
        print('GANHADOR')
    elif jogador == 3:  # tesoura
        print('PERDEDOR')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 1:
        print('PERDEDOR')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('GANHADOR')
    else:
        print('JOGADA INVALIDA')

elif computador == 3:
    if jogador == 1:
        print('GANHADOR')
    elif jogador == 2:
        print('PERDEDOR')
    elif jogador == 3:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
