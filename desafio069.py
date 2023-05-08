maiores = homens = mulheres_vinte = tot = 0
while True:
    print('=-' * 15)
    print('CADASTRE UMA PESSOA')
    print('=-' * 15)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F] ')).strip().lower()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres_vinte += 1
    tot += 1
    print('=-' * 15)
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'Você cadastrou {tot} pessoas. Das quais {maiores} são maiores de idade, {homens} são homens e '
      f'{mulheres_vinte} são mulheres com menos de 20 anos de idade!')
