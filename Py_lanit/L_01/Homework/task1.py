print('Калькулятор v1.0 \n Ваc вас приветствует программа калькулятор. \n ')
chislo_1 = input("Введите, пожалуйста первое число \n")
while not chislo_1.isdigit():
    print('Укажите первое число в цифровом формате')
    chislo_1 = input('')
chislo_2 = input("введите, пожалуйста второе число \n")
while not chislo_2.isdigit():
    print('Укажите второе число в цифровом формате')
    chislo_2 = input('')
import summ
