print('\033[35m=-\033[m'*30)
D = int(input('Digite um numero: '))
print('\033[35m=-\033[m'*30)
R = D % 2
if R == 0:
    print('Seu numero é \033[7mpar\033[m')
else:
    print('Seu numero é \033[7mimpar\033[m')