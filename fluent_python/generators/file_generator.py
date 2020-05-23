"""
Iterate every files under a directory and print out the lines.
"""
import os
from pathlib import Path


def print_content(path):
    with open(path) as file:
        print(path)
        print("-" * len(str(path)))

        for line in file:
            print(line[: len(line) - 1])
        print()


def visit(directory=".", fun=print):
    for filename in os.listdir(directory):
        path = Path(directory, filename)

        if path.exists():
            if path.is_file():
                if path.suffix == ".py":
                    fun(path)
            else:
                visit(directory=path, fun=fun)


# visit(fun=print_content)
visit(directory="/Users/tonyzhou/Workspace/fluent_python", fun=print_content)
