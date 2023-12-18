def max_color(line, color):
    values = []
    words = line.split()
    maxm = 0
    
    for i in range(len(words)):
        if words[i] == color:
            value = words[i - 1]
            if int(value) > maxm:
                maxm = int(value)
    
    return maxm

def process_file(file_path):
    ans = 0
    counter = 0

    with open(file_path, 'r') as file:
        for line in file:
            counter += 1

            line = line.replace(':', '')
            line = line.replace(';', '')
            line = line.replace(',', '')
            red_max = max_color(line, 'red')
            green_max = max_color(line, 'green')
            blue_max= max_color(line, 'blue')

            ans += red_max * green_max * blue_max

    return ans

file_path = input('')

ans = process_file(file_path)

print(ans)
