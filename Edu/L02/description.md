Синтаксис.

• Конец строки является концом инструкции (точка с запятой не требуется).

• Вложенные инструкции объединяются в блоки по величине отступов.
Отступ может быть любым, главное, чтобы в пределах одного вложенного блока отступ был одинаков.
И про читаемость кода не забывайте. Отступ в 1 пробел, к примеру, не лучшее решение.
Используйте 4 пробела (или знак табуляции, на худой конец).

• Вложенные инструкции в Python записываются в соответствии с одним и тем же шаблоном,
когда основная инструкция завершается двоеточием, вслед за которым располагается вложенный блок кода,
обычно с отступом под строкой основной инструкции.

Основная инструкция
    Вложенный блок инструкций

L02-TS - проверил приведенный ниже код.
• Иногда возможно записать несколько инструкций в одной строке, разделяя их точкой с запятой

    a = 1; b = 2; print(a, b)


• Допустимо записывать одну инструкцию в нескольких строках.
Достаточно ее заключить в пару круглых, квадратных или фигурных скобок:

    if (a == 1 and b == 2 and
        c == 3 and d == 4): # Не забываем про двоеточие
          print('spam' * 3)

• Тело составной инструкции может располагаться в той же строке,
что и тело основной, если тело составной инструкции не содержит составных инструкций.
Ну я думаю, вы поняли :). Давайте лучше пример приведу:

    if x > y: print(x)