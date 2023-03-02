idade = int(input('Digite a idade do aluno: '))
if idade >= 0 and idade < 9:
    print('Você ainda é \033[1;31mMIRIM\033[m')
elif idade >= 9 and idade < 14:
    print('Você é \033[1;31mINFANTIL\033[m')
elif idade >=14 and idade < 19:
    print('Você é \033[1;31mJUNIOR\033[m')
elif idade >=19 and idade < 20:
    print('Você ja é \033[1;31mSÊNIOR\033[m')
elif idade > 20:
    print('Parabens você é \033[1;31mMASTER\033[m')
