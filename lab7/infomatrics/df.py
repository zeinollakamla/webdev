
n = int(input())
a = input().split()
count = 0 


for i in range(n):
    a[i] = int(a[i])

for i in range(1, n-1):
    if a[i-1] < a[i] and a[i] > a[i+1]:
        count += 1
        
print(count)
