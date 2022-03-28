# Обработка исключений.
def midle(a):
    try:
        return sum(a) / len(a)
    except ZeroDivisionError as e:
        print(f'Ошибка {e}')
        return 0
    else:
        print('все ок')
    finally:
        print('все хорошо')


print(midle([]))
