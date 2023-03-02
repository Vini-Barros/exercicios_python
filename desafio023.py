from random import randint
from time import sleep
print('\033[33m=-\033[m'*25)
n1 = int(input('Digite um numero de 0 a 5: '))
print('\033[33m=-\033[m'*25)
lista = randint(0, 5)
print('\033[31mPROCESSANDO...\033[m')
sleep(3)
if n1 == lista:
    print('Você ganhou')
else:
    print('Você perdeu')