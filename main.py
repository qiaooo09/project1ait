while True:
    numbers = input("Введите пять чисел через пробел:\n").split()

    if len(numbers) != 5:
        print("Введено некорректное количество чисел. Пожалуйста, введите пять чисел.")
        continue

    print("Выберите как вы хотите вывести эти числа:")
    print("1. В том же порядке")
    print("2. В обратном порядке")

    while True:
        choice = input()
        try:
            choice = int(choice)
            if choice == 1:
                print(*numbers)  # Вывод чисел в том же порядке
                break
            elif choice == 2:
                print(*numbers[::-1])  # Вывод чисел в обратном порядке
                break
            else:
                print("Некорректный вариант")
        except ValueError:
            print("Введите число от 1 до 2")


