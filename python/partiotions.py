import math, json
### Core Algorithm
def dyadic(suma, elements=None):
    if elements is None: elements = []
    if suma == 0:
        elements.sort()
        return elements
    i = 0
    while 2**(i + 1) <= suma:
        i += 1
    elements.append(2**i)
    return dyadic(suma - 2**i, elements)
###
open("partitions.txt", "w", encoding="utf-8").close()
N = int(input("How many elements: "))
for i in range(0, 2**N):
    with open("partitions.txt", "a") as f:
        f.write(f'{i} : {dyadic(i)}\n')