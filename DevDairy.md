## Калькулятор

### Первый этап
1. Итак, за пару недель на коленке собран макет. Местами он работает, но требует полного переосмысления.
2. Сердцем проекта является пакет Calculon, который создаётся с использованием языка python.
3. Пакет Calculon претендует на универсальность, то есть может быть использован для вычислений не только в рамках веб-сайта, но и в других проектах.
4. Весь JavaScript сгенерирован ИИ ввиду полного отсутствия опыта работы с JavaScript.
5. Первый дальнейший шаг будет касаться соглашений об именовании переменных для:
     - названий классов
     - переменных внутри классов(python)
     - переменных в html
     - переменных в JavaScript
6. Второй шаг должен касаться веток git.
7. Третий шаг должен касаться режима деббагинга в контексте flask.
8. Четвертый шаг должен касаться режима livereload для html-css и для flask.
9. На этом подготовка инфраструктуры выглядит завершенной.


### Второй этап
1. Итак, избавляемся от констант, немного подумали о когезии, отчаcти представили себе архитектуру... Пока особенно ничего нет,
   но возможно, что ожидается не такой уж и говнокод.
2. В main.py должны быть методы, которые раскладывают входящие данные по переменным в __init__ (?) и сбрасывают переменные после каждого цикла расчета
3. Получением и маршрутизацией данных с веб-морды должен заниматься другой класс - CalculonWebInterface?
4. Dynamic values: row_cost, comissioms_value, tax_value, risk_value, etc - категоризировать на static и dynamic values.


### FrontEnd
1. Файлы *.css
2. Пришло время заняться скриптами самостоятельно.
