import functools
import time


def clock(fun):
    @functools.wraps(fun)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = fun(*args, **kwargs)
        duration = time.perf_counter() - t0
        fun_name = fun.__name__
        arg_list = []
        if args:
            arg_list.append(", ".join(repr(a) for a in args))
        if kwargs:
            pairs = ["%s=%r" % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(", ".join(pairs))
        arg_str = ", ".join(arg_list)
        print("[%0.8fs] %s(%s) -> %s" % (duration, fun_name, arg_str, result))
        return result

    return clocked
