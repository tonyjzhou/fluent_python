import html
import numbers
from functools import singledispatch


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f"<pre>{content}</pre>"


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace("\n", "<br>\n")
    return f"<p>{content}</p>"


@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x})</pre>".format(n)


@htmlize.register(tuple)
@htmlize.register(set)
@htmlize.register(list)
def _(seq):
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"


def main():
    print(htmlize("hello world"))
    print(htmlize(5))
    print(htmlize([1, 2, 3]))
    print(htmlize((1, 2, 3)))
    print(htmlize({1, 2, 3}))


if __name__ == "__main__":
    main()
