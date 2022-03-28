def first(a):
    try:
        print(a)
        first(a + 1)

    except Exception as e:
        print(f'Ошибка - {e}')
        print('Переполнение стека')


def main():
    first(1)


if __name__ == '__main__':
    main()
