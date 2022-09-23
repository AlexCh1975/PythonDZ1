# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_week = int(input("Введите день недели: "))

if 0 < day_week < 8:
    if day_week < 6: print("Workday")
    else: print("Weekend")
else: print("It's not a day of the week!")