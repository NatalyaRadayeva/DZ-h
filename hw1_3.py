# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
# Пользователь ввел число 3.
user_number = int(input('Введите число n: '))
if user_number >= 10:
    print ("ERROR")
else:
    res = user_number * 123
print (res)
