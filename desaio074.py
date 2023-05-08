from random import randint

numeros = (randint(0,10), randint(0,10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Sorteei os valores {numeros}.')
'''maior = menor = cont = 0
for cont in range(0, len(numeros)):
    if cont == 0:
        maior = menor = numeros[cont]
    else:
        if numeros[cont] > maior:
            maior = numeros[cont]
        elif numeros[cont] < menor:
            menor = numeros[cont]
print(f'O menor número foi {menor} e o maior foi {maior}')'''
print(f'O maior numero foi {max(numeros)} e o menor foi {min(numeros)}.')
