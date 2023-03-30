# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4


def summa(a, b):
    if b == 0:
        return a
    return summa(a + 1, b - 1)


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > 0 and b > 0:
    print(f"{a} + {b} = {summa(a, b)}")
else:
    print("Введено отрицательное число.")
