# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

import random as rm #модуль пригодится для заполнения матриц

class Matrix(object):
    '''Класс матрицы, модель будет строиться на шаблоне из списка списков'''
    def __init__(self, row, col, num = 10) :
        #определение аттрибутов
        self.row = row #кол-во строк матрицы
        self.col = col #кол-во рядов матрицы
        #заполнение матрицы (по сути списка) рандомными элементами
        lst = []
        for i in range(row):
            lst.append([])
            for j in range(col):
                lst[i].append(rm.choice(range(1, num+1)))
        self.all = lst 

def get_Matrix(self, i, j):
    '''Получение значения ячейки по заданным индексам'''
    if i > self.row or j > self.col:
        print('Выход за пределы индексов матрицы')
        return None
    else:    
        return self.all[i-1][j-1]

def set_Matrix(self, i, j, value):
    '''Замена значения ячейки по заданным индексам на передаваемую в параметрах величину'''
    if i > self.row or j > self.col:
        print('Выход за пределы индексов матрицы')
    else:    
        #присвоение нового значения элементу двумерного массива в списке списков
        self.all[i-1][j-1] = value 

def mtr_print(self):
    '''Вывод матрицы в презентабельном виде'''
    print('Сгенерированная матрица (презентабельный вид):')
    for i in range(self.row):
        g=''
        for j in range(self.col):
            g += '{:5d}'.format(self.all[i][j])
        print(g)    


if __name__ == "__main__":  
    try:
        rw = int(input('Укажите кол-во строк генерируемой матрицы: '))
        cl = int(input('Укажите кол-во рядов генерируемой матрицы: '))
        nm = int(input('Укажите наибольшее допускаемое значение для ячейки матрицы: '))
    except:
        print('Требуется ввод целых положительных чисел!')
        exit()
    
    m1 = Matrix(rw, cl, nm)
    print('Размерность генерируемой матрицы:', m1.row,'х', m1.col)
    print('Сгенерированная матрица в виде списка списков:', m1.all)
    mtr_print(m1) #вывод матрицы презентабельного вида на экран


#Метод поиска 
    try:
        ii = int(input(f'Укажите для поиска элемента номер строки матрицы от 1 до {m1.row}: '))
        jj = int(input(f'Укажите для поиска элемента номер колонки матрицы от 1 до {m1.col}: '))
        print(f'Элемент с индексами ({ii},{jj}) =', get_Matrix(m1,ii,jj))
    except:
        print(f'Элемент с индексами ({ii},{jj}) не найден!')
#Метод замены
    try:
        ii = int(input(f'Укажите для корректировки значения элемента номер строки матрицы от 1 до {m1.row}: '))
        jj = int(input(f'Укажите для корректировки значения элемента номер колонки матрицы от 1 до {m1.col}: '))
        vv = int(input(f'Элемент с индексами ({ii},{jj}) имеет значение {get_Matrix(m1,ii,jj)}, укажите новое значение: '))
        set_Matrix(m1,ii,jj,vv) #Подменана на новое значение
        mtr_print(m1) #для визуализации изменений вывод матрицы презентабельного вида на экран
    except:
        print(f'Элемент с индексами ({ii},{jj}) не найден!')        
    
    
    # m2 = Matrix(2,2) # экземляр второй матрицы создается без передачи третьего параметра (num=10 по умолчанию)
    # print(m2.all)
    # print(get_Matrix(m2,1,2))
    # set_Matrix(m2,2,2,33)
    # print(get_Matrix(m2,2,2))
    # mtr_print(m2)