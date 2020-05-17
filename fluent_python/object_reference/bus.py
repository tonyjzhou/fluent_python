class Bus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, someone):
        self.passengers.append(someone)

    def drop(self, someone):
        self.passengers.remove(someone)


def main():
    team = ["Ben", "Tom", "Kate", "Jeff"]
    print(f"team={team}\n")

    bus1 = Bus(team)
    bus1.pick("Rob")
    print(f"team={team}")
    print(f"bus1.passengers={bus1.passengers}\n")

    bus2 = Bus()
    bus2.pick("Shane")
    print(f"team={team}")
    print(f"bus2.passengers={bus2.passengers}\n")

    bus3 = Bus()
    bus3.pick("Chad")
    print(f"team={team}")
    print(f"bus3.passengers={bus3.passengers}\n")


if __name__ == "__main__":
    main()
