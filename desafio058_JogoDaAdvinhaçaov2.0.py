from random import randint
from time import sleep

# Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
num = randint(0, 10)
sleep(1)
tentativas = 0
resp = 2
while resp != num:
    resp = int(input('Em que número pensei? '))
    tentativas += 1
    if resp < num:
        print('Você errou! É MAIS!')
    elif resp > num:
        print('Você errou! É MENOS!')
print('PARABÉNS VOCÊ ACERTOU! O computador pensou em {}!'.format(num))
print(f'Você precisou de {tentativas} tentativas!')
