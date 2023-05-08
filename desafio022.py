nome = str(input('Digite o seu nome completo: ')).strip()
# nome em maiúsculas
print(nome.upper())
# nome em minúsculas
print(nome.lower())
# quantas letras tem o nome sem espaços
cada_nome = nome.split()
so_letras = ''.join(cada_nome)
print('O nome completo tem {} letras!'.format(len(so_letras)))
# quantas letras o primeiro nome
pri_nome = cada_nome[0]
print('O primeiro nome tem {} letras!'.format(len(pri_nome)))
