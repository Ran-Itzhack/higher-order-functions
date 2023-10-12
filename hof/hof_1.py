def upper_text(text: str):
    return text.upper()


def lower_text(text: str) -> str:
    assert 3 > 2, "That is false"
    return text.lower()


def handle_text(func):
    text = func("Hello world!")
    print(text)
