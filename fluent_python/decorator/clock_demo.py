from fluent_python.decorator.clock import clock


@clock
def factorial(n: int):
    return 1 if n < 2 else n * factorial(n - 1)


def main():
    print(factorial(10))


if __name__ == "__main__":
    main()
