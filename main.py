while True:
    n1, n2, n3, n4, n5 = input("Введите пять чисел через пробел:\n").split()
    print("Выберите как вы хотите вывести эти числа:")
    print("1. В том же порядке")
    print("2. В обратном порядке")

    while True:
        choice = input()
        try:
            choice = int(choice)  # Преобразуем ввод в целое число
            if 1 <= choice <= 2:
                if choice == 1:
                    print(n1, n2, n3, n4, n5)
                else:
                    print(n5, n4, n3, n2, n1)
                break
            else:
                print("Некорректный вариант")
        except ValueError:
            print("Введите число от 1 до 2")