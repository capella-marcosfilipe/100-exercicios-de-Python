listagem = ('Lápis', 1.75, 'Borracha', 2.0, 'Caderno', 15.9, 'Estojo', 25.0, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('\033[35m==\033[m' * 15)
print('{:^25}'.format('LISTAGEM DE PREÇOS'))
print('\033[35m==\033[m' * 15)
for c in range(0, 18, 2):
    print(f'{listagem[c]:20}R$ {listagem[c+1]:.2f}')
