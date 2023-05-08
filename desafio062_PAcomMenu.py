# Recolher dados
termo = int(input('Digite o primeiro termo da Progressão Aritmética: '))
razao = int(input('Digite a razão: '))
# Fazer PA usando while
print(termo, end=' ')
c = 1
while c < 10:
    termo += razao
    print(f'{termo}', end=' ')
    c += 1
print('PAUSA')
# Novas opções
resp = ''
while resp != 'n':
    resp = str(input('Você gostaria de exibir mais alguns termos? [S/N] ')).strip().lower()[0]
    if resp == 's':
        final = int(input('Quantos termos a mais você quer ver? '))
        c = 0
        while c < final:
            termo += razao
            print(f'{termo}', end=' ')
            c += 1
        print('PAUSA')
    elif resp not in 'sn':
        print('Opção inválida. Tente novamente!')
print('PROGRAMA ENCERRADO')