from datetime import date

atual = date.today().year
maiores = 0
menores = 0
for c in range(0, 7):
    nasc = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    if (atual - nasc) < 18:
        menores += 1
    else:
        maiores += 1
print(f'Das 7 pessoas, {menores} são menores de idade e {maiores} são maiores de idade.')
