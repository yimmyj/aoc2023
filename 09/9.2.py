def differences_between_adjacent_elements(data):
    return [y - x for x, y in zip(data, data[1:])]

def track_and_sum_last_elements(data):
    iterations = 0
    history = []

    while any(data):
        history.append(data.copy())
        data = differences_between_adjacent_elements(data)
        iterations += 1

    ret = 0

    for i in range(len(history)):
        ind = len(history) - 1 - i
        #print(history[ind])
        ret = history[ind][0] - ret

    return ret

file_path = "data.txt"

s = 0

with open(file_path, 'r') as file:
    for line in file:
        str_values = line.split()
        int_values = [int(value) for value in str_values]
        s+=track_and_sum_last_elements(int_values)

print(s)

