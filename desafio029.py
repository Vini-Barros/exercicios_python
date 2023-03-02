from time import sleep
print('\033[34m-=\033[m'*20)
print('Analisador de triangulos')
print('\033[34m-=\033[m'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segindo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\033[34mAGUARDE...\033[m')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[4;32mEsses segmentos podem podem formar um triangulo\033[m')
else:
    print('\033[4;31mEsses segmentos não podem forma um triangulo\033[m')