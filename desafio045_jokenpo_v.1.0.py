from random import randint
from time import sleep

# Opções do jogo
opcoes = ['pedra', 'papel', 'tesoura']
pc = randint(0, 2)
# Menu de opções
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('\033[1mQual sua opção?\033[m '))
# Chamada de jokenpô
print('\033[42m {:15} \033[m'.format('JO'))
sleep(1)
print('\033[42m {:15} \033[m'.format('KEEEEEEEEENN'))
sleep(2)
print('\033[42m {:15} \033[m'.format('PÔ!!!'))
# Escolhas dos jogadores
print('=' * 15)
print('PC jogou {}'.format(opcoes[pc]))
print('Você jogou {}'.format(opcoes[player]))
print('=' * 15)
# Condicionais
if player == pc:
    status = '\033[7m EMPATE \033[m'
elif player == 0 and pc == 2 or player == 1 and pc == 0 or player == 2 and pc == 1:  # Opções de vitória do player
    status = '\033[30;44m VOCÊ GANHOU \033[m'
else:  # O resto é derrota.
    status = '\033[30;41m VOCÊ PERDEU \033[m'
# Quem ganhou?
print('Você jogou {} e o PC jogou {}! {}!'.format(opcoes[player], opcoes[pc], status))
