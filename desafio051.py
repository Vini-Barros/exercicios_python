from random import randint
computador = randint(0, 5)
print('Pensei em um numero de 0 a 5')
print('Você consegue adivinhar ? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite qual numero você acha que foi: '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
        print('Acertou')
    else:
        print('HAHA perdedor ')
print('Você deu {} palpites'.format(palpites))