produto=float(input('Qual valor do produto escolhido? R$'))
desconto= produto - (produto * 5/100)
print('Com o desconto de 5% o valor de R${} fica R${:.2f}'.format(produto,desconto))