# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

print("Введите размер плитки шоколада n x m:")
n, m, k = int(input("n = ")), int(input("m = ")), int(input("Количество долек: "))
if k <= m * n and ((k % m == 0) or (k % n == 0)):
    print("yes")
else:
    print("no")
