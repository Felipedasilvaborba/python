nome=str(input('Digite seu nome completo: ')).strip()
n=nome.split()
print('Muito prazer em te conhecer {}!!'.format(nome.capitalize()))
print('Seu primeiro nome é: {}'.format(n[0]))
print('E seu ultimo nome é: {}'.format(n[len(n)-1]))