with open("input", "r") as f:
    file = list(map(int, f.read().splitlines()))


def one():
    count = 0
    for i in range(len(file)):
        try:
            if file[i] < file[i+1]:
                count += 1
        except IndexError:
            pass
    print(count)


def two():
    count = 0
    for i in range(len(file)-3):
        if sum(file[i:i+3]) < sum(file[i+1:i+4]):
            count += 1

    print(count)
