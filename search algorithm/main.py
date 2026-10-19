
from bfs import bfs
from dfs import dfs

maze = [
    "S...#",
    ".#..#",
    ".#...",
    "...#.",
    "##..E"
]

def find_point(maze, point):
    for r, row in enumerate(maze):
        for c, value in enumerate(row):
            if value == point:
                return (r, c)

start = find_point(maze, 'S')
end = find_point(maze, 'E')

def show_maze(maze, path):
    result = [list(row) for row in maze]

    if path:
        for r, c in path:
            if result[r][c] not in ('S', 'E'):
                result[r][c] = '*'

    for row in result:
        print(''.join(row))

print("=== BFS ===")
path_bfs = bfs(maze, start, end)
if path_bfs:
    show_maze(maze, path_bfs)
    print("Jumlah langkah:", len(path_bfs) - 1)
else:
    print("Jalur tidak ditemukan")

print("\n=== DFS ===")
path_dfs = dfs(maze, start, end)
if path_dfs:
    show_maze(maze, path_dfs)
    print("Jumlah langkah:", len(path_dfs) - 1)
else:
    print("Jalur tidak ditemukan")
