l=float(input('Qual a largura da parede? '))
a=float(input('Qual a altura da parede? '))
area=l*a
tinta=area/2

print('Sua parede tem dimensão de {}m por {}m Sua área total é {:.2f}m²'.format(l,a,area))
print('Para pintar sua parede irá precisar de {:.2f}l de tinta'.format(tinta))