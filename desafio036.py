valor_casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Em quantos anos o comprador vai pagar a casa? '))
# Valor da prestação mensal
mensal = valor_casa / (anos * 12)

if mensal > (0.3 * salario):
    emprestimo = '\033[41m NEGADO \033[m'
else:
    emprestimo = '\033[42m APROVADO \033[m'

print('Para adquirir a casa no valor de R${:.2f} em {} meses, você pagará R${:.2f}/mês.\nPortanto o seu empréstimo '
      'foi {}!'.format(valor_casa, (anos * 12), mensal, emprestimo))
