n1 = float(input('Digite o primeiro lado: '))
n2 = float(input('Digite o segundo lado: '))
n3 = float(input('Digite o terceiro lado: '))
equilatero = n1 == n2 == n3 and n2 == n1 == n3 and n3 == n1 == n2
escaleno: n1 != n2 != n3 != n1
if equilatero:
    print('Seu triangulo é Equilatero!')
elif n1 != n2 != n3 != n1:
    print('Seu triangulo é Escaleno!')
else:
    print('Seu triangulo é Isoceles')