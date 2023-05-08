print('==LIQUIDAÇÃO==')
p = float(input('Preço do produto = R$'))
#desconto = preço - 5%
d = p * 0.05
print('Na promoção ele custará R${:.2f}!'.format(p-d))
