from time import sleep
ano=int(input('\033[36mDigite um ano para saber se ele é bissexto: '))
print('\033[4;40;0mO ano escolhido foi {}'.format(ano))
print('\033[33mANALISANDO...')
sleep(3)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[32mO ano {} é Bissexto!!'.format(ano))
else:
    print('\033[31mO ano {} não é Bissexto!!'.format(ano))