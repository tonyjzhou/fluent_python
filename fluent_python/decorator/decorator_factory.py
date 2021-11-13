import sys

registry = set()


def register(active=True):
    def decorator(func):
        print(f"running register(active={active}) -> decorator({func}) ...")
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorator


@register(active=False)
def f1():
    print(f"running {sys._getframe().f_code.co_name} ...")


@register()
def f2():
    print(f"running {sys._getframe().f_code.co_name} ...")


def f3():
    print(f"running {sys._getframe().f_code.co_name} ...")


def main():
    print(f"registry={registry}")
    f1()
    f2()
    f3()
    print(f"registry={registry}")


if __name__ == "__main__":
    main()
