tot_idade = 0
media_idade = 0
mais_velho = 0
homem_velho = ''
mulheres = 0
for c in range(0, 4):
    print(f'PERFIL DA {c + 1}ª PESSOA:')
    nome = str(input(f'Digite o nome: ')).strip().title()
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'Digite o sexo (M/F): ')).lower().strip()
    print('>>' * (c + 1))
    tot_idade += idade
    media_idade = tot_idade / 4
    if c == 1 and sexo == 'm':
        mais_velho = idade
        homem_velho = nome
    if sexo == 'm' and idade > mais_velho:
        mais_velho = idade
        homem_velho = nome
    if sexo == 'f' and idade < 20:
        mulheres += 1
print(f'A média de idade do grupo é {media_idade}.')
print(f'O homem mais velho do grupo é {homem_velho} que tem {mais_velho} anos.')
print(f'{mulheres} mulheres têm menos de 20 anos.')
