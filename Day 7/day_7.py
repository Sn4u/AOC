from statistics import median

with open("input", "r") as f:
    file = list(map(int, f.read().split(",")))


def one():
    med = int(median(file))
    cost = sum(map(lambda x: abs(med - x), file))
    print(cost)


def two():
    def cost(distance):
        return distance * (distance + 1) // 2

    fuels = set()
    for i in range(min(file), max(file)):
        fuels.add(sum(cost(abs(crab - i)) for crab in file))

    print(min(fuels))
