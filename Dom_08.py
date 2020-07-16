# Напишите функцию, которая читает и распечатывает текстовый файл.
#Напишите декоратор к этой функции, который печатает название файла и количество слов в нем
import os


def file_info(func):
    def wrapper(*args):
        number = 0
        file = func(*args)
        path = '.'
        file_list = os.listdir(path)
        txt_file = list()
        ext = '.txt'
        for f in file_list:
            if ext in f:
                file_name = str(f)
                name = file_name.split('.')
                print(name[0])
        for w in file:
            word_num = w.split(',')
            number = number +1
        return number
    return wrapper


@file_info
def file_reader():
    with open("text.txt", 'r') as text_file:
        file = text_file.readlines()
        print(file)
    return file


print(file_reader())

