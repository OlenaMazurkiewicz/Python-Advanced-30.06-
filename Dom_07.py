#1. Напишите функцию, которая возвращает список файлов из директории.
#2. Напишите декоратор для этой функции, который распечатает все файлы с
#раcширением .log из найденных

import os


def log_files(func):
    def wrapper(*args):
        log_file = list()
        ext = '.log'
        file_list = func(*args)
        for f in file_list:
            if ext in f:
                log_file.append(f)
        return log_file
    return wrapper


@log_files
def file_list():
    path = '.'
    files = os.listdir(path)
    return files

print (file_list())