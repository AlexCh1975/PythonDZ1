# 4. Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y). 
# *Пример:*

# in 1 out x>0, y>0;
# in 3 out x<0, y<0;
# in 33 out "The quarter is entered incorrectly!"

def out_print(text):
    print(text)

quarter = int(input("Введите четверть: "))

if quarter < 0 or quarter > 4: out_print("The quarter is entered incorrectly!") 
elif quarter == 1: out_print("x > 0, y > 0")
elif quarter == 2: out_print("x < 0, y > 0")
elif quarter == 3: out_print("x < 0, y < 0")
elif quarter == 4: out_print("x > 0, y < 0")
