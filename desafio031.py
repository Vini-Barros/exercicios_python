n1 = int(input('Digite um numero: '))
print('''Escolha uma dessas formas de conversão:
[1] Binario
[2] Octal
[3] Hexadecimal''')
escolha = int(input('Sua escolha é: '))
if escolha == 1:
    print('{} O numero Binario vale {}'.format(n1, bin(n1)[2:]))
elif escolha == 2:
    print('{}nO numero Octal vale {}'.format(n1, oct(n1)[2:]))
elif escolha == 3:
    print('{} O numero Hexadecimal vale {}'.format(n1, hex(n1)[2:]))