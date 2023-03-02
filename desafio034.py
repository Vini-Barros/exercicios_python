from  time import sleep
media1 = 5
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
r1 = (n1 + n2) / 2
print('\033[32mPROCESSANDO...\033[m')
sleep(3)
if r1 < media1:
    print('Você foi reprovado! que pena')
elif r1 >= 5 and r1 < 7:
    print('Poxa foi por pouco, mas você terá que fazer uma recuperação')
elif r1> 7:
    print('PARABENS, você foi aprovado!')
print('Sua media final foi \033[1;34m{}\033[m'.format(r1))