distancia = float(input('Qual é a distância da sua viagem em km? '))
# Usando a condição indentada do Python
'''if distancia <= 200:
    custo = distancia * 0.50
else:
    custo = distancia * 0.45'''
custo = distancia * 0.50 if distancia <= 200 else distancia *0.45 # Usando a condição simplificada do Python
print('Sua viagem de {}km custará R${:.2f}!'.format(distancia, custo))
