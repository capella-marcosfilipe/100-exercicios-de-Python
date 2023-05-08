from random import choice

aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
# Eu fiz uma lista de strings aqui embaixo! Usa-se [] para criar listas no Python
alunos = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(alunos)
print('O aluno escolhido foi o aluno {}!'.format(escolhido))
