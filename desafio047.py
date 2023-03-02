import datetime
now=datetime.datetime.now()
pn=1
nm=0
pnn=0
nothing=0
for n in range(0, 7):
    ano=int(input("Digite o Ano de Nascimento da {}ª Pessoa: ".format(pn)))
    pn+=1
    if now.year-ano<20:
        nm+=1
    else:
        nothing=0
    if now.year-ano<0:
        pnn+=1
    else:
        nothing=0
if nm==1:
    ps=''
    ps3='u'
else:
    ps='s'
    ps3='ram'
print("{} Pessoa{} Ainda Não Atingi{} a Maioridade ".format(nm, ps, ps3))
if pnn==1:
    ps2=''
    ps4='u'
else:
    ps2='s'
    ps4='ram'
if pnn>0:
    print("E {} Pessoa{} Ainda não Nasce{} ;-; ".format(pnn, ps2, ps4))