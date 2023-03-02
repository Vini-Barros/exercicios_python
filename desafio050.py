sexo = str(input('Digite seu sexo [F/M]: '))
while sexo not in 'MmFf':
    sexo = str(input('Sexo invalido tente novamente: ')).strip().upper()[0]
    if sexo == 'Ff':
        sexo = 'Feminino'
    if sexo == 'Mm':
        sexo = 'Masculino'
print('Sexo {} registrado'.format(sexo))