red_cap = 12
green_cap = 13
blue_cap = 14

def check_color(line, color, cap):
    values = []
    words = line.split()
    
    for i in range(len(words)):
        if words[i] == color:
            value = words[i - 1]
            if int(value) > cap:
                return False
    
    return True

def process_file(file_path):
    ans = 0
    counter = 0

    with open(file_path, 'r') as file:
        for line in file:
            counter += 1

            line = line.replace(':', '')
            line = line.replace(';', '')
            line = line.replace(',', '')
            red_bool = check_color(line, 'red', red_cap)
            green_bool = check_color(line, 'green', green_cap)
            blue_bool = check_color(line, 'blue', blue_cap)
            if (red_bool and green_bool and blue_bool):
                print(counter)
                ans += counter

    return ans

file_path = input('')

ans = process_file(file_path)

print(ans)
