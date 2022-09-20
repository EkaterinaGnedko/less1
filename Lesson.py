year = int(input("Введите год рождения: "))
month = int(input("Введите месяц рождения: "))
day = int(input("Введите день рождения: "))
pres_year = int(input("Введите текущий год: "))
pres_month = int(input("Введите текущий месяц: "))
pres_day = int(input("Введите текущий день: "))
y = pres_year - year
m = month - pres_month
d = pres_day - day
if m >= 12:
    y -= 1
    d >= 31
print(y)


