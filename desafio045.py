n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
D = n1 + (10 - 1) * n2
for c in range(n1, D+1, n2):
    print('{}'.format(c), end='\033[31m➡\033[m')
print('FIM')