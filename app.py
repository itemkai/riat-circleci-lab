"""Простое приложение-калькулятор для демонстрации CI/CD в CircleCI."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return a / b


def average(numbers):
    if not numbers:
        raise ValueError("Список чисел пуст")
    return sum(numbers) / len(numbers)


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(expression):
    """Вычисляет выражение вида '2 + 3'."""
    left, op, right = expression.split()
    if op not in OPERATIONS:
        raise ValueError(f"Неизвестная операция: {op}")
    return OPERATIONS[op](float(left), float(right))


if __name__ == "__main__":
    print(calculate(input("Выражение (например, 2 + 3): ")))
