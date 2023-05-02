# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

# Пункт D. РЕШЕНИЕ(модуль datetime)
import datetime
def min_in_sec(mi): #Трансформируем длительность трека из минут в секунды
    return  mi // 1 * 60 + round((mi-int(mi))*100)

def seconds_in_str(datetime_string): #Перевод секунд в формат даты H:M:S     
    return datetime.timedelta(seconds = datetime_string)

import random #импорт модуля random
# Пункт A. РЕШЕНИЕ (список)
i, time_songs, name_songs = 0, 0.00, '' # служебные переменные
while i < 3: #цикл по 3-м итерациям
    v = random.randint(0, len(my_favorite_songs)-1) #рандомный индекс из диапазона набора треков
    name_songs += my_favorite_songs[v][0] + (', ' if i < 2 else '') #собираем подстроку из рандомных треков для вывода в print
    time_songs += min_in_sec(my_favorite_songs[v][1]) #суммируем длительность воспроизведения 3-хтреков в секундах
    i += 1
time_songs = seconds_in_str(time_songs)  
#Вывод ответа по пункту А
print('Пункт A:\n','Три песни (', name_songs,') звучат ', time_songs, ' минут')

# Пункт B. РЕШЕНИЕ(словарь)
i, time_songs, name_songs = 0, 0.00, '' # служебные переменные
while i < 3: #цикл по 3-м итерациям
    z = random.randint(0, len(my_favorite_songs_dict)-1)
    y=0
    for k, v in my_favorite_songs_dict.items(): #получение ключей и значений словаря
        if  y == z:#если позиция словаря равна рандомному индексу, то подсуммируем переменные
            name_songs +=  k + (', ' if i < 2 else '') #ключ словаря -Трек
            time_songs += min_in_sec(v) #значение словаря -длительность с переводом в секунды
            break
        y += 1
    i += 1    
#Вывод ответа по пункту B
time_songs = seconds_in_str(time_songs)  
print('Пункт B:\n','Три песни (', name_songs,') звучат ', time_songs, ' минут')

# Пункт С. Недостаточно вводных данных для понимания задачи... Из-чего генерить случайные песни???
# Это собственно уже было сделано в A и B
# Ниже решение, как я это понял:
print('Пункт C:\n','Генерация случайной песни из списка my_favorite_songs- ', random.choice(my_favorite_songs)[0])
print(' Генерация случайной песни из словаря my_favorite_songs_dict- ', random.choice(list(my_favorite_songs_dict.keys())))