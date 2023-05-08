maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input(f'Digite o peso da {c + 1}ª pessoa em Kg: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso
print(f'O menor peso foi {menor}Kg e o maior peso foi {maior}Kg.')
