print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
quantos = int(input('Quantos termos você quer ver? '))
# Eu já conheço os dois primeiros termos que são 0 e 1
termo_a = 0
termo_b = 1
# Eu quero conhecer o termo seguinte, logo termo_c
termo_c = 0
# Se o usuário quiser 1 e 2 eu apresento, pois já sei.
if quantos == 1:
    print(f'{termo_a}')
elif quantos == 2:
    print(f'{termo_a} {termo_b}')
# Se o usuário quiser mais que 2, eu faço um laço.
else:
    # Já printo os termos que conheço
    print(f'{termo_a} {termo_b}', end=' ')
    # Começo o laço com um contador 2, pois já tenho 2 termos, que vai até quanto o usuário pediu.
    cont = 2
    while cont < quantos:
        # O termo seguinte será a soma dos anterior. Para o 3º termo, ele será 2 (1+1).
        termo_c = termo_a + termo_b
        # Já printo o termo seguinte.
        print(f'{termo_c}', end=' ')
        # Daí, o primeiro termo passa a ser o segundo (1 > 1).
        termo_a = termo_b
        # E o segundo termo passa a ser o terceiro (1 > 2),
        # fazendo com que o termo_c seja recalculado na próxima (2 + 1 = 3)
        termo_b = termo_c
        # Acrescento ao contador para o laço repetir o quanto queor.
        cont += 1