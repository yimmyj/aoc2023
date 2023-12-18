from queue import Queue
import sys
sys.setrecursionlimit(50000)

file_path = "test.txt"

arr = []
x = 0
y = 0

startx = 0
starty = 0

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace('\n', '')
        str_values = list(line)
        x = len(line)
        for i in range(x):
            if str_values[i] == 'S':
                startx = i
                starty = y
        arr.append(str_values)
        y+=1


arr[starty][startx] = 'F'

visited =  [[0] * x for _ in range(y)]



q = Queue()

q.put([starty, startx])


while not q.empty():
        cur = q.get()
        cury, curx = cur

        # Check if the current position is out of bounds or already visited
        if curx >= x or curx < 0 or cury >= y or cury < 0 or visited[cury][curx] != 0:
            continue

        visited[cury][curx] = 1

        # Explore neighbors based on the content of the cell
        if arr[cury][curx] == '|':
            q.put([cury-1, curx])
            q.put([cury+1, curx])
        elif arr[cury][curx] == '-':
            q.put([cury, curx+1])
            q.put([cury, curx-1])
        elif arr[cury][curx] == 'F':
            q.put([cury, curx+1])
            q.put([cury+1, curx])
        elif arr[cury][curx] == 'J':
            q.put([cury-1, curx])
            q.put([cury, curx-1])
        elif arr[cury][curx] == 'L':
            q.put([cury-1, curx])
            q.put([cury, curx+1])
        elif arr[cury][curx] == '7':
            q.put([cury+1, curx])
            q.put([cury, curx-1])


for i in range(len(visited)):
    for j in range(len(visited[i])):
        if arr[i][j] == '.':
            visited[i][j] = 0

def flood_fill(i, j, new_value):
    if i < 0 or i >= len(visited) or j < 0 or j >= len(visited[0]) or visited[i][j] != 0:
        return

    visited[i][j] = new_value
    

    # Recursively fill neighboring cells
    flood_fill(visited, i - 1, j, new_value)
    flood_fill(visited, i + 1, j, new_value)
    flood_fill(visited, i, j - 1, new_value)
    flood_fill(visited, i, j + 1, new_value)



    for j in range(len(visited[0])):
        if visited[0][j] == 0:
            flood_fill(0, j, 2)

    # Bottom edge
    for j in range(len(visited[0])):
        if visited[-1][j] == 0:
            flood_fill(len(visited) - 1, j, 2)

    # Left edge
    for i in range(len(visited)):
        if visited[i][0] == 0:
            flood_fill(i, 0, 2)

    # Right edge
    for i in range(len(visited)):
        if visited[i][-1] == 0:
            flood_fill(i, len(visited[0]) - 1, 2)

def flood_fill(visited, i, j, new_value):
    if i < 0 or i >= len(visited) or j < 0 or j >= len(visited[0]) or visited[i][j] != 0:
        return

    visited[i][j] = new_value

    # Recursively fill neighboring cells
    flood_fill(visited, i - 1, j, new_value)
    flood_fill(visited, i + 1, j, new_value)
    flood_fill(visited, i, j - 1, new_value)
    flood_fill(visited, i, j + 1, new_value)

def flood_fill_edges(visited, new_value):
    rows, cols = len(visited), len(visited[0])

    # Top edge
    for j in range(cols):
        if visited[0][j] == 0:
            flood_fill(visited, 0, j, new_value)

    # Bottom edge
    for j in range(cols):
        if visited[rows - 1][j] == 0:
            flood_fill(visited, rows - 1, j, new_value)

    # Left edge
    for i in range(rows):
        if visited[i][0] == 0:
            flood_fill(visited, i, 0, new_value)

    # Right edge
    for i in range(rows):
        if visited[i][cols - 1] == 0:
            flood_fill(visited, i, cols - 1, new_value)

flood_fill_edges(visited, 1)

def count_zeros(array):
    count = 0
    for row in array:
        for element in row:
            if element == 0:
                count += 1
    return count

print(visited)
print(count_zeros(visited))
