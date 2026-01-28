"""Test type annotations in function definitions."""


def add(a, b):
    """
    Docstring for add

    :param a: Description
    :param b: Description
    """
    return a + b


def main():
    """Run example calculation for add function."""
    x = 5
    y = 10

    result = add(x, y)
    print(result)


if __name__ == "__main__":
    main()
