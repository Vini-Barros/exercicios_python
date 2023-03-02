ano = 2018
alistamento = 18
nascimento = int(input('Digite o ano de nascimento: '))
idade = ano - nascimento
if idade < alistamento:
    print('Você ainda não pode se alistar!')
    print('Ainda falta {} anos'.format(alistamento - idade))
elif idade == alistamento:
    print('Já esta na hora de se alistar!')
elif idade > alistamento:
    print('Já passou da hora de se alistar!')
    print('Ja passou {} anos'.format(idade - alistamento))