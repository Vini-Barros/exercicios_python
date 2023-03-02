print('-' * 25)
print('Sequencia de fibonacci')
print('-' * 25)
n1 = int(input('Digite quantos termos você quer que eu mostre: '))
t1 = 0
t2 = 1
print('{} ➡ {}'.format(t1, t2), end='')
cont = 3
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        t3 = t1 + t2
        print('➡ {}'.format(t3), end=' ')
        t1 = t2
        t2 = t3
        cont = cont + 1
    print('\033[36mEspere...\033[m')
    mais = int(input('Digite mais quantos termos você quer: '))
print('Sequencia finalizada, mostrando {} termos'.format(total))
print('\033[31mFIM\033[m')