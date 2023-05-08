peso = float(input('Qual o seu peso em quilos? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    status = 'ABAIXO DO PESO'
elif 18.5 <= imc < 25:
    status = 'PESO IDEAL'
elif 25 <= imc < 30:
    status = 'com SOBREPESO'
elif 30 <= imc < 40:
    status = 'com OBESIDADE'
elif imc >=40:
    status = 'com OBESIDADE MÓRBIDA'
print('O seu IMC é de {:.1f} e você está {}!'.format(imc, status))

# Programa extra para descobrir seu peso ideal
resp = str(input('Gostaria de saber qual seria seu peso ideal? (s/n) ')).lower()
if resp == 's':
    peso_ideal_menor = 18.5 * altura * altura
    peso_ideal_maior = 25 * altura * altura
    print('O seu maior peso ideal seria {:.1f}kg e o menor peso ideal seria {:.1f}kg!'.format(peso_ideal_maior, peso_ideal_menor))
else:
    print('Até mais!')
