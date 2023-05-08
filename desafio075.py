n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o último valor: '))
numeros = (n1, n2, n3, n4)
print('\033[31m==\033[m' * 20)
print(f'Você digitou os valores: {numeros}.')
print('\033[31m==\033[m' * 20)
print(f'O número 9 aparece {numeros.count(9)} vezes.')
if numeros.count(3) > 0:
    print(f'O número 3 foi digitado na posição {(numeros.index(3)) + 1}.')
print('Os valores pares digitados foram', end=' ')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(f'{numeros[c]}', end=' ')
