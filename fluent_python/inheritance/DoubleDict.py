import collections


class DoubleDict(collections.UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)
