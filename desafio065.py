numero = ('Zero', 'um', 'Dois', 'Tres', 'Quatro', 'Cinco',
          'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
          'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
          'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    pessoa = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= pessoa <= 20:
        break
    print('Tente novamente.')
print(f'Você digitou o numero {numero[pessoa]}')