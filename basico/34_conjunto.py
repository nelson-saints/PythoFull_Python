from tkinter import Y


x = {1, 2, 3, 4, 5, 10}
y = {6, 7, 8, 9, 10}

a = x.union(y)
b = x.intersection(y)
c = x.difference(y)
d = x.symmetric_difference(y)

print(a)
print(b)
print(c)
print(d)