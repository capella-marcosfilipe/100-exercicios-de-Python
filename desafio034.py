salario = float(input('\033[30;44m Qual é o seu salário? \033[m R$'))
if salario > 1250:
    aumento = salario + ((10 / 100) * salario)
else:
    aumento = salario + ((15/100) * salario)
print('O seu salário de \033[7;40mR${:.2f}\033[m aumentará para \033[30;42mR${:.2f}\033[m!'.format(salario, aumento))
