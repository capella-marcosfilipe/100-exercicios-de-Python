palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar','praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} tem as vogais', end=' ')
    for l in range(0, len(palavras[c])):
        if palavras[c][l] in 'aeiou':
            print(f'{palavras[c][l]}', end= ' ')
