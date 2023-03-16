# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трехзначное число: "))
digit1 = number // 100
digit2 = number % 100 // 10
digit3 = number % 10
result = digit1 + digit2 + digit3
print(result)
