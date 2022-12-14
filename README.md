# Хаy ту сгенерить 100 миллионов-миллиардов строк?
## Интродакшн
В данном гайде разобраны два схожих по смыслу, но чуть разные по реализации спосба генерации данных для 3 лабы по дазам банных. Оба плюс-минус занимают одно и тоже время (но мы не проверяли)

## Python 1
Для начала устанавливаем все необходимые библиотечки для генерации нам понадобиться mimesis, faker и pandas.
В терминале пропишите следующую команду:
```
pip install mimesis faker pandas
```
По сути mimesis и фейкер делают одно и тоже - генерируют данные и можно было бы обойтись только одним из них.
Если вам нужно генерить какие-то особые категории данных - посмотрите методы в их документациях [mimesis](https://mimesis.name/en/latest/api.html) и [faker](https://faker.readthedocs.io/en/master/providers.html). Как мне показалось у фэйкера больше категорий, но mimesis работает чуть быстрее.
Pandas используется для работы с данными, которые представлены в виде таблиц - мы будем использовать его для создания таблицы и впоследствии конвертировать эту табличку в формат csv, а уже этот файл формата csv импортировать в нашу базу данных

### Пример
Допустим нам нужно сгенерировать сущность scientist, выглядит она следующим образом:

![image](https://user-images.githubusercontent.com/55802440/204097408-92e680bd-3111-41ed-9728-5c28c2a36054.png)

Импортируем из библиотек нужные нам блоки:
```python
from mimesis import Person
from mimesis import Text
from mimesis import Food
from faker import Faker
import pandas as pd
import random
import json
```
Создаем фейкер и mimesis генераторы
```python
person = Person('ru')
rand_text = Text()
food = Food()
faker = Faker()
```
Далее напишем функцию в которую будем передавать строку с который начинается генерация и количество строчек которые мы хотим сгенерировать:
```python
def scientist(start, number_of_rows):
    return [{
        'code': x + 1,
        'name': person.first_name() + ' ' + person.last_name(),
        'degree': random.choices(degree, weights=weight_degree)[0],
        'speciality': random.choices(speciality)[0],
        'country': faker.country(),
        'workplace': faker.company(),
        'email': person.email(),
        'phone': person.telephone(),
        'menu': json.dumps({
            'breakfast': food.dish(),
            'lunch': food.dish(),
            'dinner': food.dish(),
            'drink': food.drink()
                }),
        'articles': [rand_text.title() for i in range(random.randint(1, 10))],
              } for x in range(start, start + number_of_rows, 1)
            ]
```
В первой строке мы генерируем айдишник, во второй имя и фамилию(отмечу, что генерируемые значения на русском языке, так как в генератор Person мы передавали 'ru', а также
по-хорошему здесь надо передавать параметр gender, но мы на это забьём). Третья строчка - туда передаётся массив degree, которые мы подготовили заранее и массив весов соответствующих элементов:
```python
degree = ('phd', 'bachelor', 'master', 'college', 'proffesional', 'doctoral')
weight_degree = [0.1, 0.6, 0.3, 0.4, 0.3, 0.1]
```
Далее можно отметить, что для колонки меню мы генерируем значение типа json, а для articles массив.

Теперь вызываем нашу функцию и конвертируем в csv формат с помощью функции [to_csv](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html):
Мы генерируем всю таблицу не циликом, а частями - самое оптимальное это блоками по 5-10 млн.
Генерируем по 5 млн. столбцов и **первый раз** вызываем ее так:
```python
  pd.DataFrame(scientist(0, 5000000)).to_csv('scientist.csv', index=False)
```
Все последующие разы мы добавляем строки к уже имеющемуся файлу(то есть запускам скрипт столько раз, сколько нам нужно)
Для i-ого раза:
```python
pd.DataFrame(scientist(5000000 * i, 5000000)).to_csv('example.csv', index=False, mode='a', header=False)
```
И вот спустя полчасика-час готовый файлик у вас в кармане весит он примерно ~7гб осталоь только его импортнуть в дазу банных, если у вас стоит dbeaver, то просто нажимаете правой кнопочкой мыши по иконки схемы и нажимаете импорт данных(не забудьте, что вы должны настроить типы данных для вашей таблицы самостоятельлно, так как по умолчанию для любого текста он ставит varchar).
Если вы пользуетесь PgAdmin ~~то удалите и поставьте dbeaver~~ посмотрите этот [гайд](https://hevodata.com/learn/pgadmin-import-csv/)

[Итоговый скрипт](https://github.com/proooooogiba/DataBase/blob/61cba6d283903a697fb7cb6d49b15e50f1e66514/generation.py)

## Python 2
[Михаил](https://github.com/DaMagus26) любезно создал [тетрадку](https://colab.research.google.com/drive/1oiKxNVyOgZXIHo_GgB8qKv3Q-5IPPyI5), в котором подробно разобрал, как реализовать генерацию от начала до конца. Без лишних слов просто переходим и преисполняемся.

## Ruby
Здесь должен быть вариант как заполнить дазу банных с помощью рельсов, но его пока нет :)

