print("\n Вас приветсует приложение ГАДАЛКА, котороая, безошибочно определяет ваше имя, возраст и даже местонахождение!! \n купюры сувать в CD-ROM ")

import datetime
(name, old, place , country) = (input('\n Как вас зовут? \n'),
                              int(input('Сколько вам полных лет? \n')) ,
                              input('В каком городе вы родились? \n') ,
                              input('В какой стране вы родились? \n'))
dateraw = (datetime.datetime.now().year)
date = dateraw - old

print(f"\n \n Обращаюсь к звездам...... \n \n  Уважаемый {name}! На сегодняшний день ({datetime.date.today()}) Вы проживаете в стране {country}, в городе {place}, и ВЫ родились в {date} году")