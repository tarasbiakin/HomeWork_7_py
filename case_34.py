# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:                                     Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам    Парам пам-пам

vonni_i_pttchk= input(str('Введите выражение '))#'пара-ра-рам рам-пам-папам па-ра-па-дам'
glasn = 'аоуыэуёиюяАОУЫЭЕЁИЮЯ'

def vinni(vonni_i_pttchk,glasn):
    data = list(map(str,vonni_i_pttchk.split()))
    # print(data)
    list_1=[]
    list_2 =['Парам пам-пам','Пам пара']
    for test in data:
        list_1.append((len(list(filter(lambda x: x in glasn, test)))))

    # print(list_1)

    if list_1.count(list_1[0]) == len(list_1):
        return list_2[0]
    else:
        return list_2[1]   


print(vinni(vonni_i_pttchk,glasn))
