def square(a, n):
    return pow(a, n)

a, n = (int(i) for i in input().split())

print(square(a, n))
