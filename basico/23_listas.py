nomes = ['Caio', 'Marcos', 'Carlo', 'Pedro','Nelson', 'Amanda']

#nomes.insert(5, 'João')
#insere o valor dentro da lista conforme a posição informada

#nomes.pop(0)
#remove o valor dentro da lista conforme a posição informada.

#nomes.remove('Caio')
#remove o primeiro valor informado dentro da lista

#print(nomes.index('Carlo'))
#index informa a posição do elemento informado dentro da lista

nomes.sort(reverse=True)
#ordena lista em ordem alfabetica e numerica

nomes_ordenado = sorted(nomes)
#função que cria uma nova lista ordenada com base na selecionada
print(nomes_ordenado)

print(nomes)