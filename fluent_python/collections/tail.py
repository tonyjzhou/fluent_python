from collections import deque


def tail(file_name):
    with open(file_name) as f:
        return deque(f, 10)


def main():
    process("str_key_dict.py")


def process(file_name):
    display(file_name, tail(file_name))


def display(file_name, lines):
    print(f"Last {len(lines)} lines of {file_name} are ...")
    print("".join(lines))


if __name__ == "__main__":
    main()
