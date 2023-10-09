def calculatePostfixExpression(input_string: str) -> int:
    """Алгоритм вычисления выражения, записанного в обратной польской записи
    Не поддерживает переменные"""
    operations = {"+", "-", "/", "*"}  # множество операций
    stack_of_numbers = []
    number = []  # для хранения многосимвольного числа
    for current_symbol in input_string:
        # Если текущий символ - операция или пробел и если набралось число
        if (current_symbol == " " or current_symbol in operations) and number:
            stack_of_numbers.append(int(''.join(number)))  # добавляем число в стек
            number = []  # освобождаем массив

        if current_symbol in operations:  # если встречаем операцию, то достаем 2 числа и производим операцию
            second_number = stack_of_numbers.pop(-1)
            first_number = stack_of_numbers.pop(-1)
            res = first_number + second_number  # для сложения
            if current_symbol == "-":  # для вычитания
                res = first_number - second_number
            elif current_symbol == "/":  # для деления
                res = first_number / second_number
            elif current_symbol == "*":  # для умножения
                res = first_number * second_number
            stack_of_numbers.append(res)
        elif current_symbol != " ":  # если символ - число
            number.append(current_symbol)
    return stack_of_numbers[-1]


if __name__ == "__main__":
    assert calculatePostfixExpression("1 2 +") == 3
    assert calculatePostfixExpression("6 9 + 5 - 8 1 2 * + / 7 +") == 8
    assert calculatePostfixExpression("60 3 / 542 + 23 43 * - 75 +") == -352
    assert calculatePostfixExpression("33 11 + 44 / 0 - 213 * 22 + 43 2222 - * 512 1000 * +") == -65
    print("All tests passed")
