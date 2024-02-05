print("Пробейте штрихкод:(или CTRL+C для выхода) \n")
while True:
    file_1 = open("file.txt", "a")
    a = str(input())
    b = len(a)
    c = a[:16]
    d = c[-12:]
    d1 = c[-11:]
    i = d[:3] + "-" + d[-9:]
    f = d1[:3] + "-" + d[-8:]
    if b < 14:
        print('Извините, штрих код не подходит, попробуйте другой')
    elif b < 16:
        print(f, file=file_1)
    elif b > 40:
        print('Извините, штрих код не подходит, попробуйте другой')
    else:
        print(i, file=file_1)

