soma = tot = 0
n = int(input('Digite um valor: [999 para parar] '))
while n != 999:
    soma += n
    tot += 1
    n = int(input('Digite um valor: [999 para parar] '))
print(f'Você digitou {tot} valores que somam {soma}.')
