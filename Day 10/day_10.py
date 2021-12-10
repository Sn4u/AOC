with open("input", "r") as f:
    file = f.read().splitlines()

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

other_score = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

match = {"(": ")",
         "[": "]",
         "{": "}",
         "<": ">"}


def one():
    total = 0

    def p():
        while True:
            for i in range(len(line)):
                try:
                    if match[line[i]] == line[i + 1]:
                        line.pop(i), line.pop(i)
                        print("".join(line))
                        break
                except KeyError:
                    return scores[line[i]]

                except IndexError:
                    return 0

    for line in file:
        line = list(line)
        total += p()
    print(total)


def two():
    totals = []

    def k():
        while True:
            for i in range(len(line)):
                try:
                    if match[line[i]] == line[i + 1]:
                        line.pop(i), line.pop(i)
                        break
                except KeyError:
                    return

                except IndexError:
                    return line

    def compute_score(completed):
        score = 0
        for c in reversed(completed):
            score *= 5
            score += other_score[c]
        return score

    for line in file:
        line = list(line)
        line = k()
        if line is None:
            continue
        totals.append(compute_score(line))
    print(sorted(totals)[len(totals)//2])
