# Конвертер

функция bin() - Встроенная в Python функция bin() преобразует целое (десятичное) число в двоичную (бинарную) строку с префиксом '0b'.
```
x = 10
print(bin(x))
# => 0b1010
```


TODO: Надо сделать, чтобы он не только целые числа переводил, но и дробные, например 1.4
для этого можно использовать float, но почему то print(bin(x)) требует чтобы число было integer