n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
    if i == 0 or i % 2 ==0:
        print(a[i])