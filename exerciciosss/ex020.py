frase=input('Escreva seu nome commpleto: ')

print('-----Análisando seu nome...\n')
print('Seu nome escrito maisculo fica {}'.format(frase.upper()))
print('Seu nome escrito minusculo fica {}'.format(frase.lower()))
print('Seu nome Tem um total de {} letras'.format(len (frase) - frase.count(' ')))
print('Seu primeiro nome Tem um total de {} letras'.format(len (frase [0:6])))

print('\n-----Dados analisados encerrando...')