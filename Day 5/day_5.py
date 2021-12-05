import numpy as np

with open("input", "r") as f:
    file = f.read().splitlines()

data = [a.replace(" ", "").split("->") for a in file]


def one():
    m = np.zeros(shape=(1000, 1000), dtype=int)
    for vent in data:
        x1, y1 = [int(a) for a in vent[0].split(",")]
        x2, y2 = [int(a) for a in vent[1].split(",")]

        if x2 < x1:
            x2, x1 = x1, x2

        if y2 < y1:
            y2, y1 = y1, y2

        if x1 == x2:  # vertical line
            for space in range(int(y1), int(y2) + 1):
                m[int(x1), int(space)] += 1

        elif y1 == y2:
            for space in range(int(x1), int(x2) + 1):
                m[int(space), int(y1)] += 1

    print(np.count_nonzero(m > 1))


def two():
    m = np.zeros(shape=(1000, 1000), dtype=int)
    for vent in data:
        x1, y1 = [int(a) for a in vent[0].split(",")]
        x2, y2 = [int(a) for a in vent[1].split(",")]
        if x1 == x2 or y1 == y2:
            if x2 < x1:
                x2, x1 = x1, x2

            if y2 < y1:
                y2, y1 = y1, y2

        if x1 == x2:  # vertical line
            for space in range(y1, y2 + 1):
                m[int(x1), space] += 1

        elif y1 == y2:  # horiz. line
            for space in range(x1, x2 + 1):
                m[space, y1] += 1

        else:  # diag line
            xrange = range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1)
            yrange = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
            for x, y in zip(xrange, yrange):
                m[x, y] += 1
    print(np.count_nonzero(m > 1))
