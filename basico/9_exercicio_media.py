#Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior ou igual que 6)
# Se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi 
# Reprovado (nota menor do que 4)

n1= int(input('Digite sua N1: '))
n2= int(input('Digite sua N2: '))
n3= int(input('Digite sua N3: '))
n4= int(input('Digite sua N4: '))

media = (n1+n2+n3+n4) /4
print(f'Sua nota final é: {media}')

if media >= 6:
    print('Foi Aprovado !!')
elif media >= 4:
    print('Está de Recuperação !!')
else:
    print('Está Reprovado !!')