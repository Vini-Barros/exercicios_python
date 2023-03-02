preco = float(input('Digite o valor do produto: '))
print('''Escolha sua forma de pagamento:
[1] A vista: dinheiro/cheque 10% de desconto
[2] A vista no cartão: 5% de desconto
[3] Em 2x no cartão: Preço normal
[4] Em 3x ou mais no cartão: juros de 20%''')
escolha = int(input('Escolha sua forma de pagamento: '))
if escolha == 1:
    print('Seu produto terá um desconto de 15% passando a custa {} reais'.format(preco - (preco * 10/100)))
elif escolha == 2:
    print('Seu produto tera um desconto de 5% passando a custa {} reais'.format(preco - (preco * 5/100)))
elif escolha == 3:
    print('Seu preço continuara normal sendo de {} reais'.format(preco))
elif escolha == 4:
    print('Você terá que pagar um juros de 20% no valor do seu procuto passando a custa {} reais'.format(preco + (preco * 20/100)))