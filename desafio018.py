from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))
print('O ângulo {}º tem o seno {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}!'
      .format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
