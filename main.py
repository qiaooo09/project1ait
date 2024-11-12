while True:
  numbers = input("Введите пять чисел через пробел:\n").split()

  if len(numbers) != 5:
    print("Введено некорректное количество чисел. Пожалуйста, введите пять чисел.")
    continue

  print("Выберите как вы хотите вывести эти числа:")
  print("1. В том же порядке")
  print("2. В обратном порядке")
  print("3. Сумма чисел") # Добавлено: пункт меню для суммы

  while True:
    choice = input()
    try:
      choice = int(choice)
      if choice == 1:
        print(*numbers) # Вывод чисел в том же порядке
        break
      elif choice == 2:
        print(*numbers[::-1]) # Вывод чисел в обратном порядке
        break
      elif choice == 3:
        total = sum(float(num) for num in numbers)
        print(f"Сумма чисел: {total}") # Добавлено: вычисление и вывод суммы
        break
      else:
        print("Некорректный вариант")
    except ValueError:
      print("Введите число от 1 до 3")

