print('=-' * 15)
print('    MERCADO SÃO MARCOS    ')
tot = produto_mil = menor_preco = cont = 0
while True:
    print('=-' * 15)
    print('Cadastro de compras')
    print('=-' * 15)
    produto = str(input('NOME DO PRODUTO: ')).strip().title()
    preco = float(input('PREÇO: R$'))
    cont += 1
    tot += preco
    if preco > 1000:
        produto_mil += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = produto
    resp = ' '
    while resp not in 'sn':
        resp = str(input('Deseja cadastrar mais produtos: [S/N] ')).strip().lower()[0]
    if resp == 'n':
        break
print(f'TOTAL DA COMPRA: R${tot:.2f}'
      f'\nPRODUTOS MAIS CAROS QUE R$1000,00: {produto_mil}'
      f'\nPRODUTO MAIS BARATO: {produto_barato} custando R${menor_preco:.2f}')
