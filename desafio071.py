palavras = ('Escola', 'Aprender', 'Programar', 'Futuro', 'Ensinar',
            'Bilhete', 'Mercado', 'Trabalhar', 'Estudar', 'Curso', 'parelelepipedo', 'Bia', 'Basquete')
for p in palavras:
    print(f'\nNa palavra \033[31m{p.upper()}\033[m temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
