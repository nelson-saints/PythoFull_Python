arquivo = open('pessoas.txt', 'r')
# i = 0
# while True:
#     if i > 4:
#         break
#     arquivo.write(input('Digite o nome da pessoa:') + ' ' + input('Digite a idade:') + '\n')
#     i += 1


resultados = arquivo.readlines()
x = []
for i in resultados:
    x.append(i.split())
print(x)
arquivo.close()