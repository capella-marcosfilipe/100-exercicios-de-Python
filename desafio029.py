print('-=-=-=-=-=-=- DETRAN -=-=-=-=-=-=-=-')
vel = int(input('Qual a sua velocidade em km/h? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('VOCÊ FOI MULTADO EM R${},00 \nPOR EXCEDER O LIMITE PERMITIDO!'.format(multa))
else:
    print('Continue dirigindo com cuidado!')

