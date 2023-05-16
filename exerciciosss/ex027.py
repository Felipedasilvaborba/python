vel=float(input('Qual a velocidade do seu veíulo? '))
maxima = 80
multa= (vel-80)*7
if vel<= maxima:
    print('\nTenha um bom dia, dirija com segurança! ')
else:
    print('MULTADO!!,  você está acima da maxima de {}Km/h \nVocê recebera uma Multa de R${:.2f}'.format(maxima,multa))