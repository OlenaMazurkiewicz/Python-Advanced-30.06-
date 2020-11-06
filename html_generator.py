# Напишите декоратор для превращения функции print в генератор html-тегов
# Декоратор должен принимать список тегов italic, bold, underline
# Результатом работы декоратора с аргументами italic, bold должно быть преобразование
# из строки вида "test string" в "<i><b>test string</b></i>"

def str_to_html(tags):
    def decorator(func):
        tag_base = {
            "italic": f"<i>%text%</i>",
            "bold": f"<b>%text%</b>",
            "underline": f"<u>%text%</u>",
        }

        def wrapper(text):

            open_tag = ("<i>", "<b>")
            close_tag = ("</i>", "</b>")
            core = "{open_tag}{text}{close_tag}"

            for tag in tags:
                if tag == "bold":
                    text = core.format(open_tag=open_tag[1], text=text, close_tag=close_tag[1])


                if tag == "italic":
                    pattern = tag_base.pop(tag)
                    subpattern = pattern.split('%')
                    open_subpattern = str(subpattern[0])
                    close_subpattern = str(subpattern[2])
                    text = core.format(open_tag=open_subpattern, text=text, close_tag=close_subpattern)
            return text
        return wrapper
    return decorator


@str_to_html(["italic", "bold"])
def get_text(text):
    return text

res =  get_text("test string")
print(res)