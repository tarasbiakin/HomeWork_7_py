# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.


# Ввод: print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36 


from math import log10

numRows = int(input('Число строк '))
numColumns = int(input('Число колонн '))

def print_operation_table(operation, numRows, numColumns):
    if operation(1,1)==2:
        print(1,end='\t')

    colSize = int(log10(operation(numRows+1, numColumns+1)))+2#размер колонки вычисляется таким хитрым способом и передается в печать

    for row in range(1, numRows+1):
        for column in range(1, numColumns+1):
            if operation(1,1)==2:
                column=column-1
            print("{:>{}}".format(operation(row,column), colSize), end='\t')
        print()

# передаем лямбду и значения 
print_operation_table(lambda x, y: x * y,numRows,numColumns)