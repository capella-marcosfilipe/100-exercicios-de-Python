from random import randint
from time import sleep

num = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
resp = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if resp == num:
    print('PARABÉNS VOCÊ ACERTOU! O computador pensou em {}!'.format(num))
else:
    print('TENTE NOVAMENTE! O número era {}!'.format(num))
