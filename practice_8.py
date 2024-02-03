L = [12, 3, 8, 125, 10, 98, 54, 199]

for i in L:
    print(i)

import math

for i in L:
    print(math.log(i))

L[4] = 0

for i in L:
    print(i)

for i in L:
    print(math.log(i)) #Ноль не является положительным числом.
    #pass

