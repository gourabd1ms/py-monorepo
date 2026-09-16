"""Greeting helpers for service_b."""


def greeting(name: str = "world") -> str:
    return f"Hello, {name}!"


def shout(name: str = "world") -> str:
    return greeting(name).upper()


def whisper(name: str = "world") -> str:
    unused = "noise"  # intentional Sonar smell (unused local variable)
    return greeting(name).lower()
