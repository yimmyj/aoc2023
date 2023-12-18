text = []
gears = {}

def process_file(file_path):

    with open(file_path, 'r') as file:
        for line in file:
            text.append(line)

def find_number_indices(line):
    result = []
    start_index = None

    for i, char in enumerate(line):
        if char.isdigit():
            if start_index is None:
                start_index = i
        elif start_index is not None:
            result.append([start_index, i - 1])
            start_index = None

    if start_index is not None:
        result.append([start_index, len(line) - 1])

    return result

def has_adjacent_symbol(line_number, start, end):

    x_start = max(0, line_number - 1)
    x_end = min(len(text), line_number + 2)
    y_start = max(0, start - 1)
    y_end = min(len(text[line_number]), end + 2)

    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if not text[i][j].isdigit() and text[i][j] != '.' and text[i][j] != '\n':
                key = (i,j)
                if key not in gears:
                    gears[key] = []
                gears[key].append(int(text[line_number][start:end+1]))

file_path = 'test.txt'

process_file(file_path)

for i in range(len(text)):
    ranges = find_number_indices(text[i])

    for j in ranges:
        has_adjacent_symbol(i, j[0], j[1])

filtered_keys = [gears[key][0] * gears[key][1] for key in gears.keys() if len(gears[key]) == 2]
print(sum(filtered_keys))