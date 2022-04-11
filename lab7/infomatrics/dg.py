
n = int(input())
a = input().split()
temp = 0 


for i in range(n):
    a[i] = int(a[i])

if n % 2 == 0:
    for i in range(n//2):
        temp = a[n-1-i]
        a[n-1-i] = a[i]
        a[i] = temp
    
    for i in range(n):
        print(a[i], end = " ")

else: 
    for i in range((n-1)//2):
        temp = a[n-1-i]
        a[n-1-i] = a[i]
        a[i] = temp
    for i in range(n):
        print(a[i], end = " ")
