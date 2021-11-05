class MarcoCommand:
    def __init__(self, commands):
        self._commands = list(commands)

    def __call__(self, *args, **kwargs):
        for c in self._commands:
            c()
