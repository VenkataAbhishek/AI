from collections import deque

def BFS(start):
    visited= set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex,end=" ")
            visited.add(vertex)
            queue.extend([n for n in graph[vertex] if n not in visited])

graph = {
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],'E':['F'],'F':[]
}

BFS('A')