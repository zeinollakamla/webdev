n = int(input())
a = input().split()
count = 0

for i in range(n):
    a[i] = int(a[i])

for i in range(1, n):
    if a[i]>a[i-1]:
        count += 1
    
print(count)       