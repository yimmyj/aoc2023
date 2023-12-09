import re
from math import gcd
d = ""
m = {}
file_path = "data.txt"
starts = []
ends = []
lc = 0

with open(file_path, 'r') as file:
    for line in file:
        if lc == 0:
            d = line
        lc+= 1
        if lc > 2:
            matches = re.match(r'(\w+) = \((\w+), (\w+)\)', line)
            if matches:
                a1, a2, a3 = matches.groups()
                m[a1] = [a2, a3]
                if (a1[2] == 'A'):
                    starts.append(a1)
                if (a1[2] == 'Z'):
                    ends.append(a1)

vals = []

for i in starts:
    cur = i
    c = 0

    while (cur not in ends):
        ind = c % (len(d)-1)
        print(cur, ind, d[ind])

        if (d[ind] == 'L'):
            cur = m[cur][0]
        else:
            cur = m[cur][1]
        c+= 1
    vals.append(c)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_array(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)

    return result

result_lcm = lcm_of_array(vals)

print(result_lcm)