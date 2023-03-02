n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Mais um: '))
lista = [n1, n2, n3]
r1 = max(lista)
r2 = min(lista)
if r1:
    print('\033[7;40mO seu maior numero é {:.1f} e seu menor numero é {:.1f}\033[m'.format(r1, r2))