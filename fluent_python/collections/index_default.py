import collections
import re


def main():
    index = index_file("str_key_dict.py")
    output(index)


def output(index):
    for word in sorted(index, key=str.lower):
        print(word, index[word])


def index_file(file_name: str) -> dict:
    index = collections.defaultdict(list)

    with open(file_name) as f:
        for row_no, line in enumerate(f, 1):
            for match in re.finditer("\\w+", line):
                word = match.group()
                col_no = match.start() + 1
                location = (row_no, col_no)
                index[word].append(location)

    return index


if __name__ == "__main__":
    main()
