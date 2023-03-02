from time import sleep
import random
pay_dentista = 0
print('''TRABALHOS:
[1] Dentista
[2] Advogado
[3] Engenheiro
[4] Professor''')

player = int(input('Escolha um trabalho: '))

if player == 1:
    dias = [3, 4, 5]
    print('Você é dentista !')
    print('-=' * 30)
    print('DIA 1')
    print('-=' * 30)
# Serviço 1
    print('Um novo paciente chegou...')
    servico_1 = str(input('Você irá atendelo ?'))
    print('-' * 60)

    if servico_1 == 'S':
        print('-' * 60)
        print('Atendendo paciente...')
        print('-' * 60)
        sleep(5)
        print('Você atendeu um paciente com sucesso!')
        print('Você recebeu R$ 100.00 reais pela consulta')
        pay = 100
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

    elif servico_1 == 'N':
        print('O paciente foi embora...')
        print('Você não ganhou nada')
        print(f'Total arrecadado: {pay_dentista} reais')

    sleep(15)


# Serviço 2
    print('-=' * 30)
    print('Um paciente novo chegou sem hora marcada...')

    servico_2 = str(input('Atende-lo ?'))
    print('-' * 60)

    if servico_2 == 'S':
        print('-' * 60)
        print('Atendendo paciente...')
        print('-' * 60)
        sleep(5)
        print('paciente atendido com sucesso!')
        print('Você recebeu R$150.00 reais pela consulta fora de hora!')
        pay = 150
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

    elif servico_2 == 'N':
        print('O paciente não foi atendido e foi embora...')
        print('Você não recebeu nada.')
        print(f'Total arrecadado: {pay_dentista} reais')

    sleep(15)

# Serviço 3
    print('-=' * 30)
    print('Paciente em estágio final do tratamento das 16:00 horas chegou!')
    servico_3 = str(input('Vamos atende-lo ?'))
    print('-' * 60)

    if servico_3 == 'S':
        print('''Terminar tratamento ?
        [S] Sim(+750 por finalizar na hora)
        [N] Não(+1.050 na proxima consulta)''')
        escolha_1 = str(input('Faça sua escolha: '))
        print('-' * 60)

        # Escolha 1
        if escolha_1 == 'S':  # Finalizar na hora
            print('Finalizando tratamento...')
            print('-' * 60)
            sleep(5)
            print('Paciente foi atendido com sucesso!')
            print('Você recebeu R$750.00 reais por ter finalizado o paciente!')
            pay = 750
            pay_dentista += pay
            print(f'Total arrecadado: {pay_dentista} reais')

        elif escolha_1 == 'N':  # Terminar procedimento na proxima consulta
            print('Atendendo paciente...')
            print('-' * 60)
            sleep(10)
            print('Paciente finalizado com sucesso!')
            print('Você recebeu R$300.00 reais pela consulta!')
            pay = 300
            pay_dentista += pay
            print(f'Total arrecadado: {pay_dentista} reais ')

    elif servico_3 == 'N':
        print('O paciente foi embora...')
        print('Você recebeu R$300.00 pela visita!')

# Serviço 4
    print('-=' * 30)
    print('Paciente querendo fazer branqueamento(18:00)')
    servico_4 = str(input('Fazer procedimento ? [S/N]'))
    print('-' * 60)
    if servico_4 == 'S':
        print('''
        [1] Branqueamento normal(R$500)
        [2] Branqueamento permanente(R$1000)''')

        escolha_2 = int(input('Escolha o tipo de procedimento: '))
        print('-' * 60)
        if escolha_2 == 1:  # Branqueamento Normal
            print('Realizando procedimento...')
            print('-' * 60)
            sleep(10)
            print('Processo realizado com sucesso!')
            print('Você recebeu R$500.00 pelo procedimento')
            pay = 500
            pay_dentista += pay
            print(f'Total arrecadado: {pay_dentista} reais')

        elif escolha_2 == 2:  # Branqueamento permanente
            print('Fazendo Branqueamento permanente...')
            print('-' * 60)
            sleep(15)
            print('Branqueamento concluido !')
            print('Você recebeu R$1000.00 pelo tratamento')
            pay = 1000
            pay_dentista += pay
            print(f'Total arrecadado: {pay_dentista} reais')

    if servico_4 == 'N':
        print('O paciente foi embora indignado...')
        print('Você recebeu apenas R$100.00 pela visita')
        pay = 100
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

# Serviço 5
    print('-=' * 30)
    print('Paciente das 19:00 colocar aparelho!')
    servico_5 = str(input('Colocar aparelho ?[S/N]'))
    print('-' * 60)

    if servico_5 == 'S':
        print('Realizando procedimento...')
        print('-' * 60)
        sleep(10)
        print('Aparelho bucal colocado com sucesso!')
        print('Você recebeu R$600.00 pelo procedimento')
        pay = 600
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

    elif servico_5 == 'N':
        print('O paciente retornará outro dia')
        print('Você recebeu 200 pela visita!')
        pay = 200
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

    print('-=' * 30)
    print('DIA 2')
    print('-=' * 30)

    print('''(Hora: 10:00 AM)
    - Paciente operar siso''')
    servico_6 = str(input('Operar [S/N] ? '))

    if servico_6 == 'S':
        print('Operando...')

        sleep(5)

        print('Paciente operado com sucesso !')
        print('Você recebeu R$850.00 pela operação!')

        pay = 850
        pay_dentista += pay

        print(f'Total arrecadado: {pay_dentista} reais')
        print('Devido essa operação ser fragil será preciso marcar um retorno')

        retorno = random.randint(3, 5)

        escolha_3 = str(input(f'Marcar dia {retorno} o retorno ? '))

        agenda = []
        agenda.append(retorno)

        if escolha_3 == 'S':
            print('Retorno agendado com sucesso!')

        else:
            while (escolha_3 == 'N'):
                escolha_3 = str(input(f'Dia indisponivel, tente novamente: '))

    elif servico_6 == 'N':
        print('Você perdeu um paciente...')
        print('Você recebeu 100 reais pela visita ')
        pay = 100
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

    print('''(13:00 PM)
    - Paciente: Manutenção no aparelho e escovação profunda''')
    servico_7 = str(input('Fazer os procedimentos ? [S/N]'))
    if servico_7 == 'S':
        print('Fazendo manutenção no aparelho...')
        sleep(5)
        print('Fazendo escovação profunda!')
        sleep(1)
        caries = str(input('''OPS! Você acho carie nos dentes da paciente
        [S] Tirar as caries (150 + 450)
        [N] Não tirar as caries(+450)
        Escolha: '''))
        if caries == 'S':
            print('Removendo caries...')
            pay = 600
            pay_dentista += pay
            print(f'Total arrecadado: {pay_dentista} reais')
        elif caries == 'N':
            print('Terminando escovação profunda...')
            sleep(4)
            print('Você recebeu R$450.00 pelo serviço')
            pay = 450
            pay_dentista += pay
            print(f'Total arrecadado: {pay_dentista} reais')
    elif servico_7 == 'N':
        print('Paciente foi embora do consultorio!')
        print('Você recebeu R$100 pela visita')
        pay = 100
        pay_dentista += pay
        print(f'Total arrecadado: {pay_dentista} reais')

    print('''(14:00 PM)
    - Trapper quer fazer grillz !!''')
    servico_8 = str(input('Fazer Grillz ?'))

    if servico_8 == 'S':
        material = int(input('''
        [1] ICE(R$3000)
        [2] OURO(R$1500)
        [3] PRATA(R$1000)
        Escolha o material que será usado: '''))
        if material == 3:
            print('Fazendo grillz...')
            sleep(10)
            pay = 1000
            pay_dentista += pay
            print('Finalizado!')
            print(f'Total arrecadado: {pay_dentista} reais')

        else:
            while material != 3:
                print('Material errado !!')
                material = int(input('Tente novamente, escolha o material: '))
elif player == 2:
    pay_adv = 0

    print('Você é um Advogado !')
    print('-'*30)
    servico_adv = str(
        input('Um novo processo como advogado surgiu! Aceita ? (Y/N)'))

    if servico_adv == 'Y':
        print('Audiencia marcada e sendo realizada...')
        sleep(5)
        print('Parabens você ganhou na justuça')
        pay = 10000
        pay_adv += pay
        print('Trabalho finalizado!❤')
        print(f'Total arrecadado como advogado é de: R${pay_adv}')

elif player == 3:
    print('Você é Engenheiro ! ')
elif player == 4:
    print('Você é um Professor !')
