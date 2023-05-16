import random
from time import sleep
computador = random.randint(0,5)
print('-=-' * 25)
print('Vou pensar em um número entre 0 e 5, tente adivinhar...')
print('-=-' * 25)
jogador=int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
    print('PARABENS você ganhou!!!')
else:
    print('EU GANHEI o número era {} e não {}'.format(computador,jogador))
    