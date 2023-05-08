from datetime import date

sexo = str(input('Sexo (m/f): ')).lower()
if sexo == 'm':
    ano_nasc = int(input('Quando você nasceu? '))
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade == 18:
        print('PARTIU SE ALISTAR! Você está com 18 anos!')
    elif idade > 18:
        saldo = ano_atual-(ano_nasc + 18)
        print('PASSOU DA HORA DE SE ALISTAR! Você está {} anos atrasado.'.format(saldo))
    else:
        saldo = (ano_nasc+18)-ano_atual
        print('ESPERE! Faltam {} anos para você poder se alistar.'.format(saldo))
elif sexo == 'f':
    print('No Brasil, alistamento não é obrigatório para mulheres!')
else:
    print('Opção inválida. Tente novamente.')