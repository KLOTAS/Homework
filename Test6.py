distance = float(input("Дистанция в первый день: "))
goal = float(input("Цель: "))
days_km = 1
while distance < goal:
    distance *= 1.1
    days_km *= 1
print(f'Требуемое количество дней - {days_km}')