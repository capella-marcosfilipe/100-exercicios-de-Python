from time import sleep

print('\033[33m{:=^40}\033[m'.format(' LOJAS MARCOS '))
preco = float(input('VALOR DA COMPRA R$'))
print('\033[33m=\033[m' * 40)
print('\033[1;43m FORMAS DE PAGAMENTO: \033[m \n'
      '[1] À VISTA EM DINHEIRO/CHEQUE\n'
      '[2] À VISTA NO CARTÃO\n'
      '[3] ATÉ 2X NO CARTÃO\n'
      '[4] 3X OU MAIS NO CARTÃO')
pgto = str(input('Escolha uma opção: '))
print('PROCESSANDO SUA COMPRA...')
sleep(2)
if pgto == '1':
    novo_preco = preco - (preco * 0.1)
    print('Você tem 10% de desconto! Sua compra será de R${:.2f}!'.format(novo_preco))
elif pgto == '2':
    novo_preco = preco - (preco * 0.05)
    print('Você tem 5% de desconto! Sua compra será de R${:.2f}!'.format(novo_preco))
elif pgto == '3':
    print('Sua compra será de R${:.2f}!'.format(preco))
elif pgto == '4':
    print('O juros é de 20%! Sua compra será de R${:.2f}!'.format(preco + (preco*0.2)))
    totparc = int(input('Quantas parcelas? '))
    parcela = (preco +(preco * 0.2)) / totparc
    print('PROCESSANDO PARCELAS...')
    sleep(2)
    print('Sua compra será parcelada em {} vezes de R${:.2f}'.format(totparc, parcela))
else:
    print('Opção inválida! TENTE NOVAMENTE!')
