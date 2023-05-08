nome = 'Marcos'
# Lista de cores que vou utilizar.
# Isto aqui é um dicionário!
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\00[33m',
         'pretoebranco': '\033[7;40m'
         }
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))
