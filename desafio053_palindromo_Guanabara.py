frase = str(input('Digite uma frase: ')).strip().upper()
# Juntar todas as letras
palavras = frase.split()
junto = ''.join(palavras)
# Inverter uma palavra
inverso = ''
    # Usando fatiamento no Python
inverso = junto[::-1]
    # Usando for
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
# Teste de strings
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
