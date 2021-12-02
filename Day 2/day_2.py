with open("input", "r") as f:
    file = list(f.read().splitlines())


def one():
    dy = dx = 0
    for line in file:
        direction, distance = line.split()
        distance = int(distance)
        if direction == "forward":
            dx += distance
        elif direction == "down":
            dy += distance
        elif direction == "up":
            dy -= distance
    print(dy * dx)


def two():
    dy = dx = aim = 0
    for line in file:
        direction, distance = line.split()
        distance = int(distance)
        if direction == "forward":
            dx += distance
            dy += (aim*distance)
        elif direction == "down":
            aim += distance
        elif direction == "up":
            aim -= distance
    print(dy * dx)
