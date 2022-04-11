x = input()
num = 0

for i in range(len(x)):
    num += int(x[i])*2**(len(x)-i-1)

print(num)
