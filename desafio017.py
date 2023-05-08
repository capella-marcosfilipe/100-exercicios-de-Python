from math import hypot

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("Um triângulo retângulo com cateto oposto medindo {} e o cateto adjacente medindo {}, \ntem a hipotenusa medindo"
      " {:.2f}!".format(cateto_oposto, cateto_adjacente, hipotenusa))
