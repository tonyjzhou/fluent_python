import math
import reprlib
from array import array


class Vector:
    type_code = 'd'

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
        return hash(tuple(self))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def from_bytes(cls, my_bytes):
        type_code = chr(my_bytes[0])
        memory_view = memoryview(my_bytes[1:]).cast(type_code)
        return cls(memory_view)
