import re
d = ""
m = {}

file_path = "data.txt"

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

print(m)


c = 0
cur = "AAA"

while (cur != "ZZZ"):
    ind = c % (len(d)-1)
    print(cur, ind, d[ind])

    if (d[ind] == 'L'):
        cur = m[cur][0]
    else:
        cur = m[cur][1]
    c+= 1

print(c)