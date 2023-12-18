from queue import Queue

file_path = "data.txt"

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

print(startx, starty)
print(x, y)

arr[starty][startx] = 'L'
print(arr)

dist = [[100000] * x for _ in range(y)]
visited =  [[False] * x for _ in range(y)]

q = Queue()

q.put([starty, startx, 0])
dist[starty][startx] = 0

m = 0

while not q.empty():
        cur = q.get()
        cury, curx, curdist = cur
        print(cury, curx, curdist)

        # Check if the current position is out of bounds or already visited
        if curx >= x or curx < 0 or cury >= y or cury < 0 or visited[cury][curx]:
            continue

        # Process the current cell (optional, modify this part as needed)
        print(dist[cury][curx], curdist)
        dist[cury][curx] = min(curdist, dist[cury][curx])
        visited[cury][curx] = True
        m = curdist

        # Explore neighbors based on the content of the cell
        if arr[cury][curx] == '|':
            q.put([cury-1, curx, curdist + 1])
            q.put([cury+1, curx, curdist + 1])
        elif arr[cury][curx] == '-':
            q.put([cury, curx+1, curdist + 1])
            q.put([cury, curx-1, curdist + 1])
        elif arr[cury][curx] == 'F':
            q.put([cury, curx+1, curdist + 1])
            q.put([cury+1, curx, curdist + 1])
        elif arr[cury][curx] == 'J':
            q.put([cury-1, curx, curdist + 1])
            q.put([cury, curx-1, curdist + 1])
        elif arr[cury][curx] == 'L':
            q.put([cury-1, curx, curdist + 1])
            q.put([cury, curx+1, curdist + 1])
        elif arr[cury][curx] == '7':
            q.put([cury+1, curx, curdist + 1])
            q.put([cury, curx-1, curdist + 1])
        print(q)


print(dist)
print(m)
