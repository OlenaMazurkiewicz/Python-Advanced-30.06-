print('Task 1')

def three_biggest_int(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести 3 наибольших числа из исходного массива
    """
    m = 3

    biggest_ints = list()
    input_list.sort()

    for _ in input_list:
        if _ not in biggest_ints:
            biggest_ints.append(_)

    biggest_ints = biggest_ints[-m:]

    return biggest_ints

input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

res = three_biggest_int(input_list)
print(res)


print('Task 2')


def lowest_int_index(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести индекс минимального элемента массива
    """
    minimum = input_list[0]

    size = len(input_list)

    for i in range(size):
        if input_list[i] < minimum:
            minimum = input_list[i]

    lowest_int_index = input_list.index(minimum)

    return lowest_int_index


input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

res = lowest_int_index(input_list)
print(res)

print('Task 3')


def reversed_list(input_list):
    """
    Дан массив чисел.
    [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]
    вывести исходный массив в обратном порядке
    """
    size = len(input_list)

    for i in range(size//2):
        input_list[i], input_list[size-1-i] = input_list[size-1-i], input_list[i]

    reversed = input_list

    return reversed


input_list = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]

res = reversed_list(input_list)
print(res)

print('Task 4')


def find_common_keys(dict1, dict2):
    """
    Найти общие ключи в двух словарях, вернуть список их названий
    """
    dict1_set = set(dict1)
    dict2_set = set(dict2)

    common_keys = list(dict1_set.intersection(dict2_set))

    return common_keys


dict1 = {'name': 'Andrey', 'age': 30, 'city': 'Kiev'}
dict2 = {'name': 'Viktor', 'age': 34}

res = find_common_keys(dict1, dict2)
print(res)




student_list = [
                {'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
                {'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
                {'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
                {'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
                {'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
                {'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}
                ]

def sort_by_age(student_list):
    """
    Дан массив из словарей:
[{'name': 'Viktor', 'age': 30, 'city': 'Kiev'},
{'name': 'Andrey', 'age': 34, 'city': 'Kiev'},
{'name': 'Maksim', 'age': 20, 'city': 'Dnepr'},
{'name': 'Artem', 'age': 50, 'city': 'Dnepr'},
{'name': 'Vladimir', 'age': 32, 'city': 'Lviv'},
{'name': 'Dmitriy', 'age': 21, 'city': 'Lviv'}]

    C помощью sort() отсортировать массив из словарей
    по значению ключа 'age', сгруппировать данные по значению ключа 'city'
    вывод должен быть такого вида :
        {
           'Kiev': [ {'name': 'Viktor', 'age': 30 },
                        {'name': 'Andrey', 'age': 34}],
           'Dnepr': [ {'name': 'Maksim', 'age': 20 },
                           {'name': 'Artem', 'age': 50}],
           'Lviv': [ {'name': 'Vladimir', 'age': 32 },
                        {'name': 'Dmitriy', 'age': 21}]
        }
    """


    size = len(student_list)

    for i in range(size):
        min = i
        for j in range(i+1, size):
            if student_list[min]['age'] > student_list[j]['age']:
                min = j
        student_list[i], student_list[min] = student_list[min], student_list[i]



    sorted_dict = dict()
    for i in range(size):
        sorted_dict = student_list[i]['city']



    return sorted_dict


res = sort_by_age(student_list)
print(res)

