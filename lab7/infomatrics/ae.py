v = int(input("Скорость: "))
t = int(input("Время: "))

s = v * t % 109

print((s + 109)%109)