print('PRIMEIRO E ÚLTIMO NOME DE UMA PESSOA')
print('>-'*20)
name = str(input('Digite seu nome completo: ')).strip().upper().split()
print(f'\nMuito prazer em te conhecer, {name[0].capitalize()}!')
print(f'Seu primeiro nome é {name[0]}\nSeu último nome é {name[-1]}')
print('>-'*20)
