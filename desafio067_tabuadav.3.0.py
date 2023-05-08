while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{c:^3} x {num:^3} = {c*num:^3}')
print('PROGRAMA ENCERRADO')
