def calculatePostfixExpression(input_string: str) -> int:
    """Алгоритм вычисления выражения, записанного в обратной польской записи
    Не поддерживает переменные"""
    operations = {"+", "-", "/", "*"}
    stack_of_numbers = []
    number = []
    for current_symbol in input_string:
        if current_symbol == " " or current_symbol in operations:  # Если текущий символ - операция или пробел
            if number:
                try:
                    stack_of_numbers.append(int(''.join(number)))
                except:
                    print("Нельзя вводить строку с переменными")
                    return 0
                number = []

        if current_symbol in operations:
            second_number = stack_of_numbers.pop(-1)
            first_number = stack_of_numbers.pop(-1)
            res = first_number + second_number
            if current_symbol == "-":
                res = first_number - second_number
            elif current_symbol == "/":
                res = first_number / second_number
            elif current_symbol == "*":
                res = first_number * second_number
            stack_of_numbers.append(res)
        elif current_symbol != " ":  # если символ - число
            number.append(current_symbol)
    return stack_of_numbers[-1]


if __name__ == "__main__":
    assert calculatePostfixExpression("1 2 +") == 3
    assert calculatePostfixExpression("1 223 -") == -222
    print("All tests passed")
