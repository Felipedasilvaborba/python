s1=float(input('Qual o sálario do Felipe antes do reajuste? R$'))
s2=float(input('Qual o sálario do Edvaldo antes do reajuste? R$'))
reajustef=s1 + (s1*15/100)
reajustee=s2 + (s2*15/100)

print('--------------------REAJUSTE SÁLARIAL--------------------')

print('Com o reajuste o sálario do Felipe de R${} fica agora em R${:.2f}'.format(s1,reajustef))
print('Com o reajuste o sálario do Edvaldo de R${} fica agora em R${:.2f}'.format(s2,reajustee))