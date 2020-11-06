# Напишите функцию, которая возвращает список файлов из директории.
# Напишите декоратор для этой функции, который прочитает все файлы с
# раширением .log из найденных

import os


def log_reading(func):
    def wrapper(*args):
        log_reading = list()
        ext = '.log'
        file_list = func(*args)
        for f in file_list:
            if ext in f:
                file = open(f, 'r')
                log_reading = file.readlines()
                file.close()
        return log_reading
    return wrapper


@log_reading
def get_files(path):
    file_list = os.listdir(path)
    return file_list

res =  get_files("E:\Python Advanced")
print(res)


