from time import sleep
pay_dentista = 0
print('''TRABALHOS:
[1] Dentista
[2] Advogado
[3] Engenheiro
[4] Professor''')
player = int(input('Escolha um trabalho: '))
if player == 1:
    print('Você é dentista !')
    print('-=' * 20)
    print('DIA 1')
    print('-=' * 20)
    print('Um novo paciente chegou...')
    servico_1 = str(input('Você irá atendelo ?'))
    if servico_1 == 'S':
        print('Atendendo paciente...')
        sleep(5)
        print('Você atendeu um paciente com sucesso!')
        print('Você recebeu R$ 100.00 reais pela consulta')
        pay = 100
        pay_dentista += pay
        print(pay_dentista)

    elif servico_1 == 'NnNãonão':
        print('O paciente foi embora...')
        print('Você não ganhou nada')

    sleep(30)

    print('Um paciente novo chegou sem hora marcada...')
    servico_2 = str(input('Atende-lo ?'))
    if servico_2 == 'S':
        print('Atendendo paciente...')
        sleep(5)
        print('paciente atendido com sucesso!')
        print('Você recebeu R$150.00 reais pela consulta fora de hora!')
        pay = 150
        pay_dentista += pay
        print(pay_dentista)
    elif servico_2 == 'N':
        print('O paciente não foi atendido e foi embora...')
        print('Você não recebeu nada.')
        print(pay_dentista)

    sleep(15)

    print('Paciente em estágio final do tratamento das 16:00 horas chegou!')
    servico_3 = str(input('Vamos atende-lo ?'))
    if servico_3 == 'S':
        print('''Terminar tratamento ?
        [1] Sim(+300 na proxima consulta)
        [2] Não(+750 por finalizar na hora)''')
        escolha_1 = int(input('Faça sua escolha: '))
        if escolha_1 == 1:
            print('Atendendo paciente...')
            sleep(5)
            print('Paciente foi atendido com sucesso!')
            print('Você recebeu R$300.00 reais pela consulta!')
            pay = 300
            pay_dentista += pay
            print(pay_dentista)
        elif escolha_1 == 2:
            print('Finalizando tratamento do paciente...')
            sleep(10)
            print('Paciente finalizado com sucesso!')
            print('Você recebeu R$750.00 reais por ter finalizado o paciente!')
            pay = 750
            pay_dentista += pay
            print(pay_dentista)

elif player == 2:
    print('Você é um Advogado !')
elif player == 3:
    print('Você é Engenheiro ! ')
elif player == 4:
    print('Você é um Professor !')
