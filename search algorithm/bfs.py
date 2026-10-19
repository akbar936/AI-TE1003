
from collections import deque

def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (row, col), path = queue.popleft()

        if (row, col) == end:
            return path

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if (0 <= nr < len(maze)
                and 0 <= nc < len(maze[0])
                and maze[nr][nc] != '#'
                and (nr, nc) not in visited):

                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None
