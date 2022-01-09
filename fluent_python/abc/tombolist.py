import random

from fluent_python.abc.tombola import Tombola


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            position = random.randrange(len(self))
            return self[position]
        else:
            raise LookupError("pick from an empty TomboList")

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
