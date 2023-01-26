#Receba F para feminino e M para masculino e exiba o seco da pessoa.

sexo = input('Informe seu sexo F ou M: ')


if sexo == 'F' or sexo == 'f':
    print('Sexo Feminino.')
elif sexo == 'M' or sexo == 'm':
    print('Sexo Masculino.')
else:
    print('Valor inválido')