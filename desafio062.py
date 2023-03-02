total = homem = mulher = 0
while True:
    print('-' * 50)
    print('REGISTRE UMA PESSOA')
    print('-' * 50)
    idade = int(input('Qual sua idade ? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [F/M]: '))
        print('-'*50)
        if idade >= 18:
            total += 1
        if sexo == 'M':
            homem += 1
        if idade <= 20:
            mulher += 1
    resp = ' '
    while resp not in 'SN':
        print('-'*50)
        resp = str(input('Quer continuar [S/N]?'))
        print('-'*50)
    if resp == 'N':
        break
print(f'Tem {total} pessoas acima de 18 anos')
print(f'Foram cadastrados {homem} homens')
print(f'Tem {mulher} mulheres abaixo de 20 anos')