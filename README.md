# Task2

## Разработать программу для вычисления кратчайшего пути для почтальона.

Описание задачи.
Почтальон выходит из почтового отделения, объезжает всех адресатов один раз для вручения посылки и возвращается в почтовое отделение.

Необходимо найти кратчайший маршрут для почтальона.

Карта адресатов.

![addresses_map](https://user-images.githubusercontent.com/75761890/177194766-a78619fb-c514-4224-8513-e818fb9b1960.png)



Координаты точек:
1. Почтовое отделение – (0, 2)
2. Ул. Грибоедова, 104/25 – (2, 5)
3. Ул. Бейкер стрит, 221б – (5, 2)
4. Ул. Большая Садовая, 302-бис – (6, 6)
5. Вечнозелёная Аллея, 742 – (8, 3)

Описание решения.
Общее количество всех возможных путей проезда вычисляется по формуле (n - 1)!, где n – количество точек (адресатов).

Расчёт количества возможных маршрутов объезда адресатов для данной карты: (5 - 1)! = 4! = 24 (маршрута). Необходимо найти кратчайший маршрут и вывести последовательность точек, которые его составляют.

Для поиска такого маршрута необходимо вычислять расстояния между точками, составляющих маршрут. Это позволит найти общую длину маршрута. Путем перебора длин всех возможных маршрутов найти самый короткий из них.


Пример результата работы программы
Результат работы программы может быть оформлен следующим образом:

(0, 2) -> (2, 5)[3.605551275463989] -> (6, 6)[7.728656901081649] -> (8, 3)[11.334208176545639] -> (5, 2)[14.496485836714019] -> (0, 2)[19.49648583671402] = 19.49648583671402
