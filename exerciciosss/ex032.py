s=float(input('Digite o sálario do funcionario: R$'))
sbase = 1250.00
if s > sbase:
    aumento = (s/100)*10 + s
else:
    aumento = (s/100)*15 + s
print('O novo sálario do funcionario será R${:.2f}'.format(aumento))