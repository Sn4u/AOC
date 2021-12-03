from statistics import mode

with open("input", "r") as f:
    file = f.read().splitlines()


def one():
    gamma = ""
    for pos in range(len(file[0])):
        gamma += (mode(line[pos] for line in file))

    epsilon = "".join("0" if int(a) else "1" for a in gamma)
    epsilon = int(epsilon, 2)
    gamma = int(gamma, 2)
    print(gamma * epsilon)


def two():
    length = len(file[0])
    data = set(l for l in file)
    for pos in range(length):
        column = "".join(line[pos] for line in data)
        bit = "0" if column.count("0") > column.count("1") else "1"
        data = data - set(filter(lambda l: l[pos] == bit, file))
        if len(data) == 1:
            break
    a = (list(data)[0])

    data = set(l for l in file)
    for pos in range(length):
        column = "".join(line[pos] for line in data)
        bit = "0" if column.count("0") <= column.count("1") else "1"

        data = data - set(filter(lambda l: l[pos] == bit, file))
        if len(data) == 1:
            break

    b = list(data)[0]
    print(int(b, 2) * int(a, 2))

two()
