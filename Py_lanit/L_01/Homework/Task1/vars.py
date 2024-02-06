choise = input('Я хочу (выберите пункт):\n 1) Сложить \n 2) Вычесть \n 3) Умножить \n 4) Разделить \n 5) Выйти \n ')
if choise == '5':
    exit()
while not choise.isdigit():
    print('Выберите пункт и введите его номер (без скобочки)')
    choise = input('')
chislo_1 = input("Введите, пожалуйста первое число \n")
while not chislo_1.isdigit():
    print('Укажите первое число в цифровом формате')
    chislo_1 = input('')
chislo_2 = input("Введите, пожалуйста второе число \n")
while not chislo_2.isdigit():
    print('Укажите второе число в цифровом формате')
    chislo_2 = input('')
summ=int(chislo_1) + int(chislo_2)
sub=int(chislo_1) - int(chislo_2)
multiply=int(chislo_1) * int(chislo_2)
div=int(chislo_1) / int(chislo_2)
