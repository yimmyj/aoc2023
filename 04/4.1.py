def count_matching_integers(input_string):
    parts = input_string.split('|')

    if len(parts) == 2:
        before_set = set(int(num) for num in parts[0].split() if num.isdigit())
        after_set = set(int(num) for num in parts[1].split() if num.isdigit())

        matching_count = len(before_set.intersection(after_set))
        return matching_count

    return 0

def calc_point(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return 2*calc_point(num-1)


def process_file(file_path):
    ans = 0
    with open(file_path, 'r') as file:
        for line in file:
            result = count_matching_integers(line)
            ans += calc_point(result)

    print(ans)

process_file('test.txt')