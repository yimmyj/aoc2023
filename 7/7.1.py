cards = []

def process_file(file_path):
    ans = 0
    with open(file_path, 'r') as file:
        for line in file:
            tokens = line.split()

            cards.append(tokens)

process_file("data.txt")

def score(ss):
    s = ss[0]
    #custom_order = "AKQJT98765432"
    custom_order = "23456789TJQKA"
    
    if len(s) != 5:
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

# Custom sorting using the score function as the key
sorted_strings = sorted(cards, key=score, reverse=False)

#print("Sorted Strings:", sorted_strings)

s = 0

for i in range(len(sorted_strings)):
    s+= int(sorted_strings[i][1]) * (i+1)

print(s)

