from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = max(numeros)
menor = min(numeros)
print(f'Os numeros soteados são {numeros}')
print(f'O maior entre eles é \033[34m{maior}\033[m e o menor é \033[34m{menor}\033[m')