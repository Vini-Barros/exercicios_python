import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
Escolhido = random.choice(lista)
print('\033[1;31;mO escolhido foi {}\033[m'.format(Escolhido))