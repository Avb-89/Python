# модуль с проверкой, что возраст указан числом
age = input('сколько вам лет?: ')
while not age.isdigit():
    print('Укажите число пожалуйста')
    age = input('')

