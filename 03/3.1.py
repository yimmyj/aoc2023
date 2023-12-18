text = []

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

    # Check if a number extends to the end of the string
    if start_index is not None:
        result.append([start_index, len(line) - 1])

    return result

def has_adjacent_symbol(line_number, start, end):

    x_start = max(0, line_number - 1)
    x_end = min(len(text), line_number + 2)
    y_start = max(0, start - 1)
    y_end = min(len(text[line_number]), end + 2)

    #print(x_start, x_end, y_start, y_end)

    for i in range(x_start, x_end):
        for j in range(y_start, y_end):
            if not text[i][j].isdigit() and text[i][j] != '.' and text[i][j] != '\n':
                return True

    return False

file_path = 'test.txt'

process_file(file_path)

ans = 0

for i in range(len(text)):
    ranges = find_number_indices(text[i])

    for j in ranges:
        if (has_adjacent_symbol(i, j[0], j[1])):
            ans+=int(text[i][j[0]:j[1]+1])

print(ans)

# input_string = "467..114..8"
# indices = find_number_indices(input_string)

# print(indices)