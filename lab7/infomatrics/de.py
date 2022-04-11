
n = int(input())
a = input().split()
count = 0 


for i in range(n):
    a[i] = int(a[i])

for i in range(1, n):
    if (a[i-1] > 0 and a[i] > 0) or (a[i-1] < 0 and a[i] < 0):
        count += 1
if (count > 0):
    print("YES")
else:
    print("NO")
