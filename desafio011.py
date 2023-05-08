print('==== LOJA DE CONSTRUÇÃO ====')
l = float(input('Qual a largura da sua parede? '))
a = float(input('Qual a altura da sua parede? '))
area = l*a
baldes = area / 2
print('Você precisará comprar {0} litros de tinta para pintar {1} metros quadrados'.format(baldes, area))
