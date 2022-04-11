x = int(input("Введите число: "))
n = 0

for i in range(len(str(x))):
    digital = x % 10
    x //= 10
    n *= 10
    n += digital
print(n)
    



    