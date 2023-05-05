# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number: int) ->str:
    #pass
     #Сделаем через кортеж, с обработчиком ошибок (чтобы в случае ошибки возвращалось None)
    try:
        #возвращает элемент кортежа по индексу, совпадающему с числовым параметром number
        return ('Ноль','Один','Два','Три','Четыре','Пять','Шесть','Семь','Восемь','Девять')[number]
    except:
        return None

try: 
    #обработчик ошибки преобразования типа данных
    num = int(input('Введите число от 0 до 9: ')) #интеррактивный запрос
    print(f'switch_it_up({num}) -> {switch_it_up(num)}') #распечатаем результат функции (и здесь же вызовем её)
except ValueError:
    print('Введён недопустимый параметр')