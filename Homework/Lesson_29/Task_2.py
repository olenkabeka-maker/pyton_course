"""Використовуючи пошук в ширину, напишіть алгоритм, який може визначити найкоротший шлях 
від кожної вершини до кожної іншої вершини. Це називається задачею пошуку найкоротшого шляху для всіх пар."""

from collections import deque

def bfs_shortest_paths_from(start, graph):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if dist[neighbor] == float('inf'):
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

    return dist


def all_pairs_shortest_paths(graph):
    result = {}

    for vertex in graph:
        result[vertex] = bfs_shortest_paths_from(vertex, graph)

    return result



graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

distances = all_pairs_shortest_paths(graph)

for start in distances:
    print(f"Відстані від вершини {start}: {distances[start]}")