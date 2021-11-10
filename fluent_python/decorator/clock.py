import time


def clock(fun):
    def clocked(*args):
        t0 = time.perf_counter()
        result = fun(*args)
        duration = time.perf_counter() - t0
        fun_name = fun.__name__
        arg_str = ', '.join(repr(a) for a in args)
        print("[%0.8fs] %s(%s) -> %s" % (duration, fun_name, arg_str, result))
        return result

    return clocked
