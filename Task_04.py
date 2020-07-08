from random import randint

print('Task 1')


def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """

    word = '/catalog/'
    result_list = [string for string in url_list if word in string]

    return result_list


url_list = ['http://www.example.com/dogs/poodles/poodle1',
            'http://www.example.com/dogs/poodles/poodle2',
            'http://www.example.com/catalog/poodles/poodle3',
             'http://www.example.com/catalog/poodles/poodle4'
            ]


res = catalog_finder(url_list)
print(res)



print('Task 2')


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """

    center = len(input_str)//2

    if len(input_str) % 2 == 0:
        output_str = input_str[(center-1)] + input_str[center]
    else:
        output_str = input_str[(center-1)] + input_str[center] + input_str[(center+1)]

    return output_str


print('Input one arbitrary word')
input_str = str(input())

res = get_str_center(input_str)
print(res)


print('Task 3')


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """

    output_dict = {char: input_str.count(char) for char in input_str}

    return output_dict


print('input one arbitrary word')
input_str = str(input())

res = count_symbols(input_str)
print(res)


print('Task 4')


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """

    middle = len(str1)//2
    result_str = str1[:middle]+str2[:]+str1[middle:]

    return result_str


print('input arbitrary word #1')
str1 = str(input())

print('input arbitrary word #2')
str2 = str(input())

res = mix_strings(str1, str2)
print(res)


print('Task 5')


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """

    lst = [randint(1, 100) for _ in range(100)]

    even_int_list = [value for value in lst if value % 2 == 0]

    return even_int_list


print(even_int_generator())
