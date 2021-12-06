with open("input", "r") as f:
    file = list(map(int, f.read().split(",")))


def one():
    class Lanternfish:
        instances = []

        def __init__(self, age):
            self.instances.append(self)
            self.age = age

        def step(self):
            if self.age == 0:
                self.age = 7
                Lanternfish(9)
            self.age -= 1

    for fish in file:
        Lanternfish(fish)

    for day in range(80):
        for fish in Lanternfish.instances:
            fish.step()
    print(len(Lanternfish.instances))


def two():
    fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    new_fishes: int = 0

    for fish in file:
        fishes[fish] += 1

    for day in range(256):
        for age in range(0, 9):
            if age == 0:
                new_fishes = fishes[age]
                fishes[7] += fishes[age]
            else:
                fishes[age-1] = fishes[age]
        fishes[8] = new_fishes
        new_fishes = 0

    print(sum(fishes.values()))
