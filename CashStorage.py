#Написать свой cache декоратор c максимальным размером кеша и его очисткой при необходимости.
# Декоратор должен перехватывать аргументы оборачиваемой функции
# Декоратор должен иметь хранилище, где будут сохраняться все перехваченные аргументы и результаты выполнения декорируемой функции
# Декоратор должен проверять наличие перехваченных аргументов в хранилище. Если декорируемая функция уже вызывалась
# с такими аргументами, она не будет вызываться снова, вместо этого декоратор вернет сохраненное значение.
# Декоратор должен принимать один аргумент - максимальный размер хранилища.
# Если хранилище заполнено, нужно удалить 1 любой элемент, чтобы освободить место под новый.


def do_cache(maxsize):
    def power_cashed(func):
        power_cashed = dict()
        def wrapper(*args, **kwargs):
            if len(power_cashed) > maxsize:
                return power_cashed.popitem
            if args in power_cashed:
                return power_cashed[args]
            else:
                power_val = func(*args, **kwargs)
                return power_val
        return wrapper
    return power_cashed


@do_cache(maxsize=3)
def get_value(a, b):
    return a ** b


res = get_value(2, 4)
print(res)
