# x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
# x = list(filter(lambda x: x < 18 or x % 2 == 0, x))
# print(x)

# x = [{'nome': 'nelson', 'idade': 25}, {'nome': 'marcos', 'idade': 32}]

# x = list(filter(lambda x: x['idade'] <= 30, x ))

# print(x)

#-----------------------------#
#MAP
#x = [i for i in range(12, 26)]
x = [{'nome': 'nelson', 'idade': 25}, {'nome': 'marcos', 'idade': 22}]
x =list(map(lambda x: {'nome': x['nome'], 'idade': 'menor do que 30 anos'} if x['idade'] <30 else(x), x))

print(x)