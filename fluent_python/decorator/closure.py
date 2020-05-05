b = 7


def f1(a):
    global b
    print(a)
    print(b)
    b = 3


f1(6)


def make_averager():
    series = []

    def averager(value):
        series.append(value)
        return sum(series) / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))


def make_averager_fast():
    total = 0
    count = 0

    def averager(value):
        nonlocal total, count
        total += value
        count += 1
        return total / count

    return averager


avg = make_averager_fast()
print(avg(10))
print(avg(11))
print(avg(12))
