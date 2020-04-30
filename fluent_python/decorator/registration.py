registry = []


def register(fun):
    print(f"registering {fun}")
    registry.append(fun)
    return fun


@register
def f1():
    print("f1")


def f2():
    print("f2")


@register
def f3():
    print("f3")


def main():
    print("main")
    print(f"registry={registry}")
    f1()
    f2()
    f3()


if __name__ == "__main__":
    main()
