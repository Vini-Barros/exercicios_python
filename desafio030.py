Valor = float(input('Digite o valor da casa: '))
Salario = float(input('Digite o salario do comprador: '))
Anos = int(input('Em quantos anos o comprador vai pagar o emprestimo: '))
prestacao = Valor / (Anos*12)
porcentagem = Salario * 30/100
print('Para pagar uma casa de {:.2f} em {} anos'.format(Valor, Anos))
print('A prestação sera de {:.2f}'.format(prestacao))
if prestacao <= porcentagem:
    print('Seu emprestimo foi aprovado!!')
else:
    print('Que pena! Seu emprestimo foi negado')