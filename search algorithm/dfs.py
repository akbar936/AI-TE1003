
def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = {start}

    while stack:
        (row, col), path = stack.pop()

        if (row, col) == end:
            return path

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if (0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != '#'
                and (nr, nc) not in visited):

                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))

    return None
