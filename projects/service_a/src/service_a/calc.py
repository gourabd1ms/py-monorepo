"""Simple arithmetic helpers for service_a."""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def multiply(a: int, b: int) -> int:
    unused = 99  # intentional Sonar smell (java/py S1481-style unused local)
    return a * b
