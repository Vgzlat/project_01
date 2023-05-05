# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строки.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s: str) -> str:
    #pass
    return(s.replace('!',''))


print('Пункт A.') 
phrase = "Hi! Hello!"
print(phrase,' -> ', remove_exclamation_marks(phrase), sep='')
phrase = ""
print(phrase,' -> ', remove_exclamation_marks(phrase), sep='')
phrase = "Oh, no!!!"
print(phrase,' -> ', remove_exclamation_marks(phrase), sep='')

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s: str) -> str:
    return s[:-1] if s[-1] == '!' else s


print('\nПункт B.')
phrase = "Hi!"
print(phrase,' -> ', remove_last_em(phrase))
phrase = "Hi!!!"
print(phrase,' -> ', remove_last_em(phrase))
phrase = "!Hi"
print(phrase,' -> ', remove_last_em(phrase))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s: str) ->str: 
    s1 = s.split(' ') #разложим строку в список 
    i = 0
    while i < len(s1): #цикл по элементам списка для отбора необходимого
        if s1[i].rfind('!') == -1: # если '!' в составе элемента не найден - элемент остаётся в списке
            i += 1
        else: # если '!' у элемента найден,
            # и он единственный (т.е индекс find == индексу rfind), тогда элемент удаляется из списка
            if s1[i].find('!') == s1[i].rfind('!'): 
                del s1[i] # удаление "лишнего" элемента из списка 
            else: # если восклицательных больше одного, тогда элемент также остаётся нетронутым
                i += 1        
    #Подвернем "прореженный" список обратно в строку:
    ss = ""
    for i in s1:
        ss += ' ' + i #через пробел
    return '"' + ss + '"' #Возвращаем рез-т, обрамляя его в кавычки

#phrase = "Hi Hi! Hi!"
#phrase = "Hi! Hi!"
phrase = "Hi! Hi!! Hi!"
print(f'\nПункт С.\n"{phrase}" ===>',remove_word_with_one_em(phrase)) #Печать результата решения задачи
