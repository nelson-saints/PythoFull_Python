#Faça um programa que o usuário possa cadastrar n pessoas, armazenando seu nome, idade e altura.

cadastro = []

while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: '))
    if decisao ==2:
        break

    pessoa = {'nome': input('Digite o nome: '),
              'idade': input('Digite a idade: '), 
              'altura':input('Digite a altura: ')}
    cadastro.append(pessoa)

    
    print(cadastro)
