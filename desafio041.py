from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade <= 9:
    status = 'MIRIM'
elif 9 < idade <= 14:
    status = 'INFANTIL'
elif idade <= 19:
    status = 'JÚNIOR'
elif idade <= 25:
    status = 'SÊNIOR'
elif idade > 25:
    status = 'MASTER'

print('''IDADE: {} anos 
STATUS: \033[4m{}\033[m'''.format(idade, status))
