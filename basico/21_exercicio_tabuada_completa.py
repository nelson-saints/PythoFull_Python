#Mostre a tabuada completa de todos os número entre 1 e 10.

for i in range(1, 11):
    print(f'==========[TABUADA DO {i}]==========')
    for j in range(0, 11):
        print(f'{i} X {j} = {i * j}')