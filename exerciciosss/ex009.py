valor=float(input('Quanto dinheiro você tem na carteira? R$'))
dolar=valor/4.99

print('Com esse valor R${:.2f} você pode comprar US${:.2f} dólares'.format(valor,dolar))