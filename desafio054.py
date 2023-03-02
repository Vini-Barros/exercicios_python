primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[36m{}\033[m \033[33m\033[m➡\033[m'.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('Espere')
    mais = int(input('Você quer que eu mostre mais quantos termos ?'))
print('PA finalizada mostrandando {} termos'.format(total))
print('fim')