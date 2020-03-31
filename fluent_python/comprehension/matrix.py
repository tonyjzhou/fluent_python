def flatten(matrix):
    return [c for r in matrix for c in r]


def transpose(matrix):
    return [list(r) for r in zip(*matrix)]


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(flatten(m))
print(transpose(m))
