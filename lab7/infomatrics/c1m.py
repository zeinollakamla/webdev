n = int(input())
count = 0
x = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count += 1
print(count)