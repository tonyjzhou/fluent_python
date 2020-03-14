def add(a, b):
    """
    >>> add(1,2)
    3
    >>> add(2,2)
    4
    """
    return a + b


if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
