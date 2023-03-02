times = ('São Paulo', 'Internacional', 'Palmeiras', 'Flamengo', 'Grêmio',
         'Atletico', 'Cruzeiro', 'Corithians', 'Santos', 'Fluminense',
         'Atletico - PR', 'America - MG', 'EC - Vitoria', 'Bahia', 'Botafogo',
         'Chapecoense', 'Ceará - SC', 'Vasco de gama', 'Sport recife', 'Paraná')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('='*95)
print(f'Os 4 ultimos colocados são {times[16:]}')
print('='*95)
print(f'Os times em ordem alfabetica fica {sorted(times)}')
print('='*95)
print(f'O Chapecoense aparece na posição {times.index("Chapecoense")+1} da lista de colocados')