from datetime import datetime


# свой тип 3

def is_valid_date(date_str, date_format="%Y.%m.%d"):
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def float_or_not(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def int_or_not(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_format(object: list):
    errors = ["Введено меньше 3 значений! ", "Дата введена неверно! ", "Высота введена неверно! ",
              "Давление введено неверно! "]
    if len(object) != 3:
        print(errors[0], end='')
        return False
    elif not is_valid_date(object[0]):
        print(errors[1], end='')
        return False
    elif not float_or_not(object[1]):
        print(errors[2], end='')
        return False
    elif not int_or_not(object[2]):
        print(errors[3], end='')
        return False
    else:
        return True


print("Введите данные, следуя формату:\nГГГГ.ММ.ДД Высота(Метры, дробное) Значение(Паскали, целое)")
print("Для выхода из программы введите ...")

file = open("Database.txt", mode='a', encoding='UTF-8')

my_object = []
while True:
    my_object = input().split(' ')
    if my_object[0] == "...":
        break
    while not check_format(my_object):
        print("Попробуйте еще раз: ", end='')
        my_object = input().split(' ')
    file.write(f"Дата: {my_object[0]}\nВысота: {my_object[1]}м\nДавление: {my_object[2]}Па\n\n")

file.close()
