import functools


class BadBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, someone):
        self.passengers.append(someone)

    def drop(self, someone):
        self.passengers.remove(someone)


class GoodBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, someone):
        self.passengers.append(someone)

    def drop(self, someone):
        self.passengers.remove(someone)


def main():
    experiment1()
    experiment2()


def log(fun):
    @functools.wraps(fun)
    def log_fun(*args, **kwargs):
        head = f"Starting {fun.__name__} ..."
        print(head)
        print("-" * len(head))
        print()

        ret = fun(*args, **kwargs)

        tail = f"Finished {fun.__name__}"
        print("-" * len(tail))
        print(tail)
        print("\n")

        return ret

    return log_fun


@log
def experiment1():
    team = ["Ben", "Tom", "Kate", "Jeff"]
    print(f"team={team}\n")
    bus1 = BadBus(team)
    bus1.pick("Rob")
    print(f"team={team}")
    print(f"bus1.passengers={bus1.passengers}\n")
    bus2 = BadBus()
    bus2.pick("Shane")
    print(f"team={team}")
    print(f"bus2.passengers={bus2.passengers}\n")
    bus3 = BadBus()
    bus3.pick("Chad")
    print(f"team={team}")
    print(f"bus3.passengers={bus3.passengers}\n")


@log
def experiment2():
    team = ["Ben", "Tom", "Kate", "Jeff"]
    print(f"team={team}\n")
    bus1 = GoodBus(team)
    bus1.pick("Rob")
    print(f"team={team}")
    print(f"bus1.passengers={bus1.passengers}\n")
    bus2 = GoodBus()
    bus2.pick("Shane")
    print(f"team={team}")
    print(f"bus2.passengers={bus2.passengers}\n")
    bus3 = GoodBus()
    bus3.pick("Chad")
    print(f"team={team}")
    print(f"bus3.passengers={bus3.passengers}\n")


if __name__ == "__main__":
    main()
