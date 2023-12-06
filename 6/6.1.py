times = [44,89,96,91]
dists = [277,1136,1890,1768]

test_times = [7, 15, 30]
test_dists = [9, 40, 200]

prod = 1

for i in range(len(times)):
    numways = 0
    for j in range(times[i]+1):
        if j * (times[i] - j) > dists[i]:
            numways+= 1
    prod = prod * numways

print(prod)