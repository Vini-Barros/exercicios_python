from time import sleep
peso = float(input('Digite a peso(KG): '))
altura = float(input('Digite o altura(M): '))
IMC = peso / (altura ** 2)
print('Calculando seu Indice de Massa Corporal')
sleep(2)
if IMC <= 18.5:
    print('Vc está abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Seu peso é Ideal')
elif 25 <= IMC < 30:
    print('Você está com Sobrepeso')
elif 30 <= IMC < 40:
    print('Você é obeso')
elif IMC > 40:
    print('Você está com Obesidade Morbida')
print('Sua altura é : {}; Seu peso é: {}; E seu IMC é {:.2f}'.format(altura, peso, IMC))