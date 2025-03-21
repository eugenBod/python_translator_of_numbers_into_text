print("Добро пожаловать.\n Данная программа переводит введеные числа от пользователя"
      "в соответствующее ему слово на английском языке.")

try:
    user_input = int(input("Введите число от 1 до 5: "))
    if user_input == 1:
        result = "Соответствующее слово: one"
    elif user_input == 2:
        result = "Соответствующее слово: two"
    elif user_input == 3:
        result = "Соответствующее слово: three"
    elif user_input == 4:
        result ="Соответствующее слово: four"
    elif user_input == 5:
        result ="Соответствующее слово: five"
    else:
        result = "Неизвестное число. Введите число от 1 до 5."
except ValueError:
    print("Ошибка ввода. Введите число.")
else:
    print(result)