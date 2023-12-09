from itertools import product

cards = []

def process_file(file_path):
    ans = 0
    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split()

            cards.append(tokens)

process_file("data.txt")

custom_order = "J23456789TJQKA"

def score(ss):
    s = ss[0]
    if len(s) != 5:
        print(s)
        raise ValueError("Input string must be of length 5")

    unique_chars = set(s)

    if len(unique_chars) == 1:
        return (6, tuple(custom_order.index(char) for char in s))  # All characters are the same
    elif len(unique_chars) == 2:
        for char in unique_chars:
            count = s.count(char)
            if count == 4:
                return (5, tuple(custom_order.index(char) for char in s))  # 4 characters are the same
            elif count == 3 or count == 2:
                return (4, tuple(custom_order.index(char) for char in s))  # 3 characters are the same, other two are
    elif len(unique_chars) == 3:
        counts = sorted(s.count(char) for char in unique_chars)
        if counts[2] == 3:
            return (3, tuple(custom_order.index(char) for char in s))
        else:
            return (2, tuple(custom_order.index(char) for char in s))
    elif len(unique_chars) == 4:
        return (1, tuple(custom_order.index(char) for char in s))  # 3 characters are the same, the other two are different
    else:
        return (0, tuple(custom_order.index(char) for char in s))


def generate_combinations(n):
    numbers = range(14)  # Numbers from 0 to 13
    return list(product(numbers, repeat=n))

def score_j(ss):
    s = ss[0]
    inds = [index for index, char in enumerate(s) if char == 'J']
    if (len(inds) == 0):
        return score(ss)
    maxscore = score(["J2345",'1'])

    combs = generate_combinations(len(inds))
    a = []

    for c in combs:
        char_list = list(s)
        for i in range(len(c)):
            char_list[inds[i]] = custom_order[c[i]]
        rs = ''.join(char_list)
        aa = score([rs, s[1]])
        mod = (aa[0], tuple(0 if i in inds else val for i, val in enumerate(aa[1])))
        # for i in range(len(c)):
        #     aa[1][inds[i]] = 0
        a.append(mod)
        # if (score([rs, val]) > maxscore):
        #     maxscore = score
    a = sorted(a, reverse=True)
    return a[0]


# Example: Generate all 3-length combinations
#print(cards)
sorted_strings = sorted(cards, key=score_j, reverse=False)

s = 0

for i in range(len(sorted_strings)):
    s+= int(sorted_strings[i][1]) * (i+1)

print(s)

