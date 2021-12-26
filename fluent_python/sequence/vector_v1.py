import functools
import math
import numbers
import operator
import reprlib
from array import array


class Vector:
    type_code = 'd'
    attributes = "xyzt"

    def __init__(self, components):
        self.__components = array(self.type_code, components)

    def __iter__(self):
        return iter(self.__components)

    def __repr__(self):
        components = reprlib.repr(self.__components)
        components = components[components.find('['):-1]
        return f"Vector({components})"

    def __str__(self):
        return f"Vector{tuple(self)}"

    def __bytes__(self):
        return bytes([ord(self.type_code)]) + bytes(self.__components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        hashes = [hash(c) for c in self.__components]
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self.__components)

    def __getitem__(self, item):
        cls = type(self)

        if isinstance(item, slice):
            return cls(self.__components[item])
        elif isinstance(item, numbers.Integral):
            return self.__components[item]
        else:
            raise TypeError(f"{cls.__name__} indexes must be integers")

    def __getattr__(self, item):
        cls = type(self)
        index = cls.attributes.find(item)
        if len(item) == 1:
            if 0 <= index < len(self.__components):
                return self.__components[index]
        raise AttributeError(f"{cls} doesn't have attribute {item}")

    def __setattr__(self, key, value):
        cls = type(self)

        if len(key) == 1:
            if key in cls.attributes:
                error = f"{key} is a readonly attribute"
            elif key.islower():
                error = f"setting a single character lower case attribute {key} is forbidden"
            else:
                error = ""

            if error:
                raise AttributeError(error)
        super().__setattr__(key, value)

    @classmethod
    def from_bytes(cls, my_bytes):
        type_code = chr(my_bytes[0])
        memory_view = memoryview(my_bytes[1:]).cast(type_code)
        return cls(memory_view)
