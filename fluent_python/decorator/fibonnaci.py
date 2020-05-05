import functools


def clock(fun):
    @functools.wraps(fun)
    def clock_fun(*args, **kwargs):
        import time
        time1 = time.time()
        ret = fun(*args, **kwargs)
        time2 = time.time()
        elapsed = time2 - time1
        name = fun.__name__

        all_args = []
        if args:
            all_args.append(', '.join([repr(a) for a in args]))
        if kwargs:
            all_args.append(', '.join([f'{k}={v}' for k, v in sorted(kwargs)]))
        arg_str = ', '.join(all_args)

        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, ret))

        return ret

    return clock_fun


@functools.lru_cache
@clock
def fib(n):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(40)
