idades = [3, 5, 27, 1, 2, 45, 60, 6, 1.5]

# for i, j in enumerate(idades):
#     print(f'I = {i} j = {j}')

idades_pares = []

for i in idades:
    if i % 2 == 0:
        idades_pares.append(i)

print(idades_pares)