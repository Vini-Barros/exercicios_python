print('\033[34m*\033[m'*50)
print('\033[7mVIAGENS!!\033[m')
print('\033[34m*\033[m'*50)
V = float(input('Digite a distancia da viagem: '))
print('Você esta prestes a iniciar uma viagem de \033[36m{}Km\033[m'.format(V))
if V<=200:
 distancia1 = V * 0.50
 print('Sua viagem custara \033[35m{}\033[m'.format(distancia1))
else:
 distancia2 = V * 0.45
 print('Sua viagem custara \033[35m R${}\033[m'.format(distancia2))