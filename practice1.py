def expressionToPostfixForm(input_string: str) -> str:
    """Переводит в постфиксную запись выражение,
    поддерживаются только операторы ()+-/*"""
    input_string = input_string.replace(" ", '')
    result = []
    stack = []

    priority_dictionary = {"+": 2, "-": 2, "*": 3, "/": 3, "(": 1, ")": 1}
    variable = []  # для хранения многосимвольных переменных и чисел
    for current_symbol in input_string:  # перебираем текущий символ
        # добавим условие для работы многосимвольными переменными и числами
        if current_symbol not in priority_dictionary:
            variable.append(current_symbol)
        else:  # символ - знак операции
            if variable:
                result.append(''.join(variable))
                variable = []
            if current_symbol == '(':  # пункт в)
                stack.append(current_symbol)
            elif current_symbol == ")":  # пункт г)
                while stack and stack[-1] != "(":
                    result.append(stack.pop(-1))
                stack.pop()  # уничтожаем (
            else:
                while stack and priority_dictionary[stack[-1]] >= priority_dictionary[current_symbol]:  # пункт б)
                    result.append(stack.pop(-1))
                if not stack or priority_dictionary[stack[-1]] < priority_dictionary[current_symbol]:  # пункт а)
                    stack.append(current_symbol)
    if variable:
        result.append(''.join(variable))
    while stack:
        result.append(stack.pop(-1))
    return ' '.join(result)


if __name__ == "__main__":
    assert expressionToPostfixForm("1+2") == "1 2 +"
    assert expressionToPostfixForm("(6+9-5) / (8+1*2)+7") == "6 9 + 5 - 8 1 2 * + / 7 +"
    assert expressionToPostfixForm("(6+91-532) / (81+21*2)+75") == "6 91 + 532 - 81 21 2 * + / 75 +"
    assert expressionToPostfixForm("first_number+b/a+54*33/(12)") == "first_number b a / + 54 33 * 12 / +"
    print("All tests passed")