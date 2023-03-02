cont = soma = 0
while True:
    numero = int(input('Digite um valor: '))
    if numero == 999:
        break
    soma += numero
    cont += 1
print(f'Você digitou {cont} numeros e a soma entre eles é {soma}')