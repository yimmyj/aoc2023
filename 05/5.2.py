#Brute force lol
#10^5 iterations benchmarked at ~7s, upper bound was 10^9
#Finished in ~2 hours
def calc_mapping(ranges):
    ret = []
    for i in ranges:
        output_start = i[0]
        input_start = i[1]
        r = i[2]
        r = [output_start, input_start, r]
        ret.append(r)

    return ret

def read_map(file, rows, cols):
    map_array = [[list(map(int, file.readline().split())) for _ in range(cols)] for _ in range(rows)]
    return map_array

def read_configuration(file_path):
    configuration = {}

    with open(file_path, 'r') as file:
        while True:
            line = file.readline().strip()
            if line.startswith("seeds:"):
                configuration['seeds'] = list(map(int, line.split()[1:]))
                break

        configuration['remaining_maps'] = []
        curmap = []
        for line in file:
            if (line != '\n'):
                if (line[0].isdigit()):
                    num_arr = [int(x) for x in line.split()]
                    curmap.append(num_arr)
                else:
                    if (curmap != []):
                        configuration['remaining_maps'].append(curmap)
                        curmap = []
                 #       print(curmap)
                    
        configuration['remaining_maps'].append(curmap)

    return configuration

config_data = read_configuration('test.txt')

seeds = config_data['seeds']
maps = config_data['remaining_maps']

print("done")

mm = 0

def isValid(ans, seeds):
    ll = len(seeds)/2
    for i in range(int(ll)):
        val = seeds[2*i]
        r = seeds[2*i+1]
        if ans >= val and ans < val + r:
            return True
    return False

ans = float('inf')
for i in range(26000000, 1000000000):
    ans = i
    if (i % 1000000 == 0):
        print(i)
    for l in range(len(maps)):
        m = maps[len(maps)-1-l]
        mapping = calc_mapping(m)
        done = False
        for k in mapping:
            output_start = k[0]
            input_start = k[1]
            r = k[2]
            if not done and ans >= output_start and ans < output_start + r:
                ans = input_start + (ans - output_start)
                done = True
        if done:
            continue
    ddone = False
    if (isValid(ans, seeds)):
        print(i, ans)
        ddone = True
        break

    if (ddone):
        breal