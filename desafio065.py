soma = tot = maior = menor = 0
resp = 's'
while resp in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    tot += 1
    if tot == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    resp = str(input('Deseja continuar? [s/n] ')).strip()[0]
media = soma / tot
print(f'Você digitou {tot} números e a média entre eles é {media}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')
