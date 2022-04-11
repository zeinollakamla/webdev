import math

a = int(input())
b = int(input())

for i in range(math.ceil(a**0.5), math.ceil((b+1)**0.5)):
    print(i*i)
