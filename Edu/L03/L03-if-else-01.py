# Вводим число для определения значения
print('Введите число для определения')
a = int(input())
# Сравниваем введенное число по шкале от -5 до 5. Если число меньше -5, то это low
# Если число от -5 до 5, то это mid, если число выше 5, то high
if a < -5:
    print('Low')
elif -5 <= a <= 5:
    print('Mid')
else:
    print('High')
