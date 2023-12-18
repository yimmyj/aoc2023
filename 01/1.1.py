def extract_digits(line):
    return [int(char) for char in line if char.isdigit() and len(char) == 1]

def process_file(file_path):
    ans = []
    with open(file_path, 'r') as file:
        for line in file:
            digits = extract_digits(line)
            ans.append(digits)

    return ans

file_path = input('')

output = process_file(file_path)
sum = 0

for line_number, digits in enumerate(output, start=1):
	sum += digits[0] * 10 + digits[len(digits)-1]

print(sum)
