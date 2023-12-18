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
                    
        configuration['remaining_maps'].append(curmap)
    return configuration

config_data = read_configuration('test.txt')

seeds = config_data['seeds']
maps = config_data['remaining_maps']

print("done")

mm = 0

ans = float('inf')
for m in maps:
    mapping = calc_mapping(m)
    for i in range(len(seeds)):
        done = False
        for k in mapping:
            output_start = k[0]
            input_start = k[1]
            r = k[2]
            if not done and seeds[i] >= input_start and seeds[i] < input_start + r:
                seeds[i] = output_start + (seeds[i] - input_start)
                done = True
    #print(seeds)

print(min(seeds))