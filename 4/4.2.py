def count_matching_integers(input_string):
    parts = input_string.split('|')

    if len(parts) == 2:
        before_set = set(int(num) for num in parts[0].split() if num.isdigit())
        after_set = set(int(num) for num in parts[1].split() if num.isdigit())

        matching_count = len(before_set.intersection(after_set))
        return matching_count

    return 0

cards = []
card_counts = []

def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            cards.append(line)
            card_counts.append(1)


process_file('test.txt')

for i in range(len(cards)):
    matches = count_matching_integers(cards[i])
    numreps = card_counts[i]
    for j in range(1, matches+1):
        card_counts[i+j] += numreps

print(sum(card_counts))
print(card_counts)