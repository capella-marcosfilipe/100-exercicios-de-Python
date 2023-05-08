km = float(input('Quantos km foram percorridos com o carro? '))
dias = int(input('Quantos dias você alugou o o carro? '))
custo_total = (km * 0.15) + (dias * 60)
print('Você terá que pagar R${:.2f}'.format(custo_total))
