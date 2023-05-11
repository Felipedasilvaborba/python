import math
a=int(input('Digite o angulo que você deseja: '))
c=math.cos(math.radians(a))
s=math.sin(math.radians(a))
t=math.tan(math.radians(a))
print('No ângulo de {} o valor do seno é {:.2f}'.format(a,s))
print('No ângulo de {} o valor do cosseno é {:.2f}'.format(a,c))
print('No ângulo de {} o valor da tangente é {:.2f}'.format(a,t))