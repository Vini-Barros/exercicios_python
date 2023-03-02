resp = 'S'
num = media = cont = soma = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    cont = cont + 1
    soma = soma + num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar ?[S/N]'))
media = soma / cont
print('Você digitou {} numeros e a media entre eles é {}'.format(cont, media))
print('O maior é {} e o menor é {}'.format(maior, menor))