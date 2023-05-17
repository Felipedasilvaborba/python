v=float(input('Qual a distancia da sua Viagem? '))
vc = 200
if v <= vc:
    print('Você está prestes a fazer uma viagem de {:.2f}Km\nO preço da viagem fica R${:.2f}.'.format(v,v*0.50))
else:
    print('Você está prestes a fazer uma viagem de {:.2f}Km\nO preço da viagem fica R${:.2f}.'.format(v,v*0.45))