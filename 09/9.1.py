
def differences_between_adjacent_elements(data):
    return [y - x for x, y in zip(data, data[1:])]

def track_and_sum_last_elements(data):
    iterations = 0
    history = []

    while any(data):
        history.append(data.copy())
        data = differences_between_adjacent_elements(data)
        iterations += 1

    sum_last_elements = sum(arr[-1] for arr in history)

    return sum_last_elements

print(track_and_sum_last_elements(data))

def get_next(y_values):
    lagrange_poly = lagrange(range(len(y_values)), y_values)

    # Predicting the next term (f(i+1))
    i = len(y_values) - 1
    next_value = lagrange_poly(i + 1)
    return next_value

file_path = "data.txt"

s = 0

with open(file_path, 'r') as file:
    for line in file:
        str_values = line.split()
        int_values = [int(value) for value in str_values]
        s+=track_and_sum_last_elements(int_values)

print(s)

