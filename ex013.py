print('REAJUSTE SALARIAL')
print('='*40)
salario = float(input('Salario do Funcionário: R$'))
reajuste = salario + (salario * (15/100))
print('\nUm funcionário que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f}'.format(salario, reajuste))
print('='*40)
