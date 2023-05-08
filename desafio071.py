print('=-' * 15)
print('    BANCO SÃO MARCOS    ')
print('=-' * 15)
saque = int(input('VALOR DO SAQUE: R$'))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
'''cedulas_50 = saque // 50
prox_cedula_20 = saque % 50
if cedulas_50 > 0:
    print(f'Total de {cedulas_50} cédulas de R$50')
cedulas_20 = prox_cedula_20 // 20
prox_cedula_10 = prox_cedula_20 % 20
if cedulas_20 > 0:
    print(f'Total de {cedulas_20} cédulas de R$20')
cedulas_10 = prox_cedula_10 // 10
prox_cedula_1 = prox_cedula_10 % 10
if cedulas_10 > 0:
    print(f'Total de {cedulas_10} cédulas de R$10')
cedulas_1 = prox_cedula_1
if cedulas_1 > 0:
    print(f'Total de {cedulas_1} cédulas de R$1')'''
