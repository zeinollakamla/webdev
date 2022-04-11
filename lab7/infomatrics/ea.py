def minimum(a, b, c, d):
    m = min(a, b)
    m1 = min(m, c)
    m2 = min(m1, d)
    return m2

a, b, c, d = input().split()


print(minimum(a, b, c, d))


