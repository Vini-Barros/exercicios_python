while True:
    print('-' * 20)
    numero = int(input('Quer ver a tabuada de qual numero: '))
    if numero < 0:
        break
    print('-' * 20)
    for c in range(1, 11):
        print(f'{numero} X {c} = {numero * c}')
    print('-' * 20)
print('\033[31mPROGRAMA FINALIZADO!\033[m')