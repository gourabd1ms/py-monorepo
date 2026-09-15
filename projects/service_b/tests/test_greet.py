from service_b.greet import greeting, shout


def test_greeting_default():
    assert greeting() == "Hello, world!"


def test_greeting_name():
    assert greeting("Sonar") == "Hello, Sonar!"


def test_shout():
    assert shout("hi") == "HELLO, HI!"
