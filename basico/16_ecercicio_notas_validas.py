#Escreva um programa que recba notas de um aluno (0 - 10), caso a nota digitada esteja fora desse intervalo
#peça para o professor digitar novamente

while True:
    n1 = float(input('Digite a nota do aluno: '))
    if n1 >= 0 and n1 <= 10:
        print(f'Nota armazenada com sucesso {n1}')
        break
    
    print('Nota inválida digite novamente')
