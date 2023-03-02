from time import sleep
n = int(input('Digite um numero: '))
c = n
f = 1
print('CALCULANDO...')
sleep(3)
while c > 0:
    print('{}'.format(c), end = '')
    print(' X ' if c > 1 else '=', end=' ')
    f = f * c
    c = c -1
print('\033[31m{}\033[m'.format(f))