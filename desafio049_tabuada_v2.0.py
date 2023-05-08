print('== TABUADA ==')
n = int(input('Tabuada de: '))
print('=============')
for c in range (1, 11):
      print(f'\033[7m{c:2} x {n:2} = {c * n:3}\033[m')
