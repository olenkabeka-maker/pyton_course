#TASK 1/2
def oops():
    raise IndexError("Помилка індексу")  #якщо тут замінити на KeyError, тот помилку не перехопить і програма завершиться помилкою

def oops_1():
    try:
        oops()
    except IndexError:
        print("Я перехопив помилку IndexError!")
oops_1()