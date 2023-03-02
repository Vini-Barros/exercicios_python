s = float(input('Qual o seu salario ? '))
if s<=1.250:
    n1 = s + (s * 15/100)
    print('Seu salario é \033[1;31m{}\033[m e com aumento de 10% fica \033[1;31m{}\033[m'.format(s, n1))
else:
    n2 = s + (s * 10/100)
    print('Seu salario é \033[1;36m{}\033[m e com aumento de 15% fica \033[1;36m{}\033[m'.format(s, n2))