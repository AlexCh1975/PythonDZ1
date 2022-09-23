# 4. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y). Напишите программу, 
# которая принимает на вход координаты двух точек и находит расстояние между ними в 
# 2D пространстве.
# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def out_print(text):
    print(text)

quarter = int(input("Введите четверть: "))

if quarter < 0 or quarter > 4: out_print("The quarter is entered incorrectly!") 
elif quarter == 1: out_print("x > 0, y > 0")
elif quarter == 2: out_print("x < 0, y > 0")
elif quarter == 3: out_print("x < 0, y < 0")
elif quarter == 4: out_print("x > 0, y < 0")
