words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 

def extract_spelled_words(line):
    ans = []
    for i in range(len(line)):
        if line[i].isdigit():
            ans.append(int(line[i]))
            continue
        for j in range(3, 6):
            if ( i+ j <= len(line) and line[i:i+j] in words):
                ans.append(words.index(line[i:i+j]))
    return ans

def process_file(file_path):
    results = []
    with open(file_path, 'r') as file:
        for line in file:
            digits = extract_spelled_words(line)
            
            results.append(digits)

    return results

file_path = input('')

output = process_file(file_path)
sum = 0

for line_number, digits in enumerate(output, start=1):
	sum += digits[0] * 10 + digits[len(digits)-1]

print(sum)
