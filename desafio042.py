print('\033[7;40m  Digite o comprimento de três retas!  \033[m')
r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('\033[32mPODEM FORMAR UM TRIÂNGULO!\033[m')
    if r1 == r2 == r3:
        print('\033[1;42m Trata-se de um triângulo EQUILÁTERO! \033[m')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('\033[1;42m Trata-se de um triângulo ISÓSCELES! \033[m')
    elif r1 != r2 != r3 != r1:
        print('\033[1;42m Trata-se de um triângulo ESCALENO! \033[m')
else:
    print('\033[31mNÃO PODEM FORMAR UM TRIÂNGULO!\033[m')
