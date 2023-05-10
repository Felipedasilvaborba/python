import math
co=float(input('Informe o valor do cateto oposto: '))
ca=float(input('Informe o valor do cateto adjascente: '))
hipotenusa=math.hypot(co,ca)

print('A hipotenusa desse triangulo vale-rá {:.2f}'.format(hipotenusa))