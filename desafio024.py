from time import sleep
M = float(input('Me diga a velocidade de um carro: '))
print('\033[33mCalculando...\033[m')
sleep(3)
R = (M - 80) * 7
if M<=80:
    print('\033[36mEsta tudo bem, continue dirigindo com segurança\033[m')
else:
    print('\033[31mVOCÊ FOI PEGO NO RADAR E TERA QUE PAGAR UMA MULTA DE R${}\033[m'.format(R))