
from bfs_agent import bfs_agent
from dfs_agent import dfs_agent

def coordinator(graph, start, goal):
    print("Koordinator: memulai pencarian jalur")

    result_bfs = bfs_agent(graph, start, goal)
    result_dfs = dfs_agent(graph, start, goal)

    print("\nHasil Agen BFS:", result_bfs)
    print("Hasil Agen DFS:", result_dfs)

    if result_bfs and result_dfs:
        print("\nPanjang jalur BFS:", len(result_bfs) - 1)
        print("Panjang jalur DFS:", len(result_dfs) - 1)

        if len(result_bfs) < len(result_dfs):
            print("Koordinator: BFS menemukan jalur lebih pendek")
        elif len(result_dfs) < len(result_bfs):
            print("Koordinator: DFS menemukan jalur lebih pendek")
        else:
            print("Koordinator: panjang jalur sama")
    else:
        print("Koordinator: salah satu atau kedua agen gagal menemukan jalur")
