a = [1, 0, 9, 12, 18, 34, 89, 91, 33, 127]
b = [2, 8, 9, 11, 76, 25, 44]

print(a[0])
print(a[2])
print(a[-1])

b.append(7)

b[4] = 8

merged = a + b

c = a.copy()
c[-1] = 100
print(c)
