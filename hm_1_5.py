# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
profit = float(input('Введите значения выручки'))
cost = float(input("Введите издержки"))
if profit > cost:
    print(f"Фирма работает в прибыль. Рентабельность фирмы составила {profit / cost:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(f"прибыль в расчете на одного сторудника сотавила {profit / workers:.2f}")
elif profit == cost:
    print("Фирма работатает в ноль")
else:
    print("Фирма работает в убыток")

