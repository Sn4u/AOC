from collections import Counter

with open("input", "r") as f:
    file = f.read().splitlines()

file = list(a.split("|") for a in file)


nums = {2: 1, 3: 7, 4: 4, 7: 8}
abc = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}


def one():
    print(len([n for line in file for n in line[1].split() if len(n) in (2, 3, 4, 7)]))


def common_to(a,b):
    return list(set(b)-set(a))[0]

def two():
    total = 0
    for line in file:
        mapping: dict[str:int] = {}
        rev_mapping = {}
        r = {v: k for k, v in Counter(line[0]).items()}
        real_to_tangled = {"f": r[9], "b": r[6], "e": r[4]}

        for tang in line[0].split():
            if len(tang) in (2, 3, 4, 7):
                mapping[tang] = nums[len(tang)]
                rev_mapping[nums[len(tang)]] = tang

        real_to_tangled["a"] = common_to(rev_mapping[1], rev_mapping[7])
        real_to_tangled["c"] = list(set.difference(set(rev_mapping[1]), set(real_to_tangled["f"])))[0]
        real_to_tangled["d"] = list(set.difference(set(rev_mapping[4]), set(real_to_tangled.values())))[0]
        real_to_tangled["g"] = list(set.difference(set("abcdefg"), set(real_to_tangled.values())))[0]

        out = ""
        for word in line[1].translate({ord(v): k for k, v in real_to_tangled.items()}).split():
            for k,v in abc.items():
                if set(word) == set(k):
                    out+=(str(v))
        total += int(out)

    print(total)

two()
