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

# Example usage
visited = [
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
]

flood_fill_edges(visited, 1)

# Print the result
for row in visited:
    print(row)