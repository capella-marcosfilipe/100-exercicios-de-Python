n1 = float(input('Digite 1ª nota: '))
n2 = float(input('Digite 2ª nota: '))
m = (n1 + n2) / 2

if m < 5.0:
    status = 'REPROVADO'
elif 5.0 <= m < 7.0:
    status = 'em RECUPERAÇÃO'
elif m >= 7.0:
    status = 'APROVADO'

print('''Sua média foi {}! 
Você está {}!'''.format(m, status))
