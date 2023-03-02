frase = input('Digite uma frase: ')
print('A letra \033[1;34mA\033[m aparece \033[1;34m{}\033[m nesta frase'.format(frase.count('a')))
print('A primeira vez que a letra \033[1;32mA\033[m apareceu foi na posição \033[1;32m{}\033[m'.format(frase.find('a')))
print('A ultima vez que a letra \033[1;35mA\033[m apareceu foi na posição \033[1;35m{}\033[m'.format(frase.rfind('a')))