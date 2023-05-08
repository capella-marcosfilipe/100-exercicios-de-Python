cid = str(input('Digite o nome da sua cidade: ')).strip()
dividida = cid.upper().split()
santo = 'SANTO' in dividida[0]
print('O nome da cidade começa com "Santo"?', santo)
