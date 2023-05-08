termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão: '))
print(termo, end=' ')
for c in range (1, 10):
    termo += razao
    print(f'{termo}', end=' ')
