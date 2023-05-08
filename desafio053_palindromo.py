frase = str(input('É palíndromo? Digite: ')).strip().lower()
# Juntar as palavras antes de contar
frase_lista = frase.split()
frase_junta = ''.join(frase_lista)
# Comparador de caracteres palíndromo
comprimento = len(frase_junta)
palindromo = 0
for c in range (0, comprimento):
    # Se a primeira letra é igual a última, se a segunda é igual à penúltima, etc
    if frase_junta[c] == frase_junta[(comprimento-1)-c]:
        palindromo += 1
if palindromo == comprimento:
    print(f'A frase "{frase.title()}" é um PALÍNDROMO!')
else:
    print(f'A frase "{frase.title()}" NÃO É UM PALÍNDROMO!')
