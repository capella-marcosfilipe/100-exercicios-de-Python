termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão: '))
print(termo, end=' ')
c = 1
while c < 10:
    termo += razao
    print(f'{termo}', end=' ')
    c += 1
    