n = int(input())
a = input().split()
count = 0

for i in range(n):
    a[i] = int(a[i])
    if a[i] > 0:
        count += 1
    
print(count)