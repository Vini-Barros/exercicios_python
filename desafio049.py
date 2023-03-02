somaidade = 0
mediaidade = 0
imaior = 0
nomevelho = ''
idademulher = 0
for c in range(1, 4+1):
    print('---Pessoa {}---'.format(c))
    nome = str(input('Digite o nome do integrante: '))
    idade = int(input('Digite a idade do integrante: '))
    sexo = str(input('Escolha o sexo [F/M]: '))
    somaidade = somaidade + idade
    if c == 1 and sexo == 'M':
        imaior = idade
        nomevelho = nome
    if sexo == 'M' and idade > imaior:
        imaior = idade
        nomevelho = nome
    if sexo == 'F' and idade <= 20:
        idademulher = idademulher + 1
mediaidade = somaidade / 4
print('A media da idade do grupo é {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(imaior, nomevelho))
print('O total de mulheres com menos de 20 anos é {}'.format(idademulher))