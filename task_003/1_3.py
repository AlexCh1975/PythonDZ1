# 3. Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Координата x: "))
y = int(input("Координата y: "))

def out_quarter(number):
    print("Четверть: {}".format(number))

if x == 0 or y == 0: 
    print("Введите координаты x и y не равные 0!")
elif x > 0 and y > 0: out_quarter(1)
elif x > 0 and y < 0: out_quarter(4)
elif x < 0 and y < 0: out_quarter(3)
elif x < 0 and y > 0: out_quarter(2)

