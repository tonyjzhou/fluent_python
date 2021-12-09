from array import array


class Vector:
    type_code = 'd'

    def __init__(self, components):
        self.__components = array(self.type_code, components)

    def __iter__(self):
        return iter(self.__components)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __abs__(self):
        pass

    def __bool__(self):
        pass

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __bytes__(self):
        pass

    def from_byte(self, byte):
        pass
