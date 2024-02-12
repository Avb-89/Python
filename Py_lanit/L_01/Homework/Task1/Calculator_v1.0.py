from imp import reload

print('Калькулятор v1.0 который умеет работать с целыми числами \n Ваc приветствует программа калькулятор. \n ')
while(True):
    import vars
    reload(vars)
    if vars.choise == '1':
        import summ
    elif vars.choise == '2':
        import sub
    elif vars.choise == '3':
        import myltiply
    elif vars.choise == '4':
        import div
    else:
        print("Такого пункта в списке, к сожалению, нет")





