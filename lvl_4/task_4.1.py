# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

def close_con(connection):
  '''Функция завершения соединения с БД'''
  if connection:
    # print('Закрываю БД')
    connection.close()

try: #Обработчик ошибок на случай повторного запуска скрипта при существующей таблице Students (и прочих ошибок)
    con = sqlite3.connect("teatchers.db") #Создаём связь с БД
    cur = con.cursor() #Создаём курсор
    #создаем таблицу Students:
    cur.execute("""
    CREATE TABLE Students
    (Student_Id INTEGER NOT NULL PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    School_Id INTEGER NOT NULL)""")
    #наполяем таблицу Students данными:
    cur.execute("""
        INSERT INTO Students VALUES
            (201, 'Иван', 1),
            (202, 'Петр', 2),
            (203, 'Анастасия', 3),
            (204, 'Игорь', 4),
            (666, 'Антилох', 1)
    """)
    con.commit() #Обновление БД после изменений
except (Exception, sqlite3.Error) as error:
    print(error)  

id_S = 0 #Установим значение ID студента по умолчанию (при возможных ошибках останется параметр = 0)
try:
    #Определение списка ID для указания в качестве подсказки пользователю в строке ввода параметра:
    id = cur.execute("SELECT Student_Id FROM Students").fetchall()     
    d = '' #подготовка текста для строки ввода пользователю
    for i in range(len(id)):
        d += str(id[i][0]) + (', ' if i < len(id)-1 else '') 
    #Запрос ввода параметра id_S для последующей подстановки в SQL запрос:
    id_S = int(input(f'Введите ID студента (доступные варианты для ввода: {d}): '))
    #Текст запроса SQL c параметром id_S... (схема INNER JOIN):
    sqlquery = """
    SELECT st.Student_Id, st.Student_Name, st.School_Id, sc.School_Name 
    FROM Students st JOIN School sc 
    ON st.School_id = sc.School_Id 
    WHERE st.Student_Id = ?"""
    cur.execute(sqlquery,(id_S,)) 
    rec = cur.fetchone() #Возвращаем набор полей из единственной записи
    #Печать результата выборки:
    print (f'ID Студента: {rec[0]}\nИмя студента: {rec[1]}\nID Школы: {rec[2]}\nНазвание школы: {rec[3]}')
except:
    print('Ошибка ввода!')    
close_con(con) #Завершаем соединение с БД через ф-цию