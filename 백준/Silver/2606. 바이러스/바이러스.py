import sys
from collections import deque

n = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

def bfs(matrix, start, visited):
    queue = deque([start])
    visited[start] = True
    result = 0
    
    while queue:
        v = queue.popleft()
        result += 1
        for i in range(n + 1):
            if not visited[i] and matrix[v][i] == 1:
                queue.append(i)
                visited[i] = True
                
    return result - 1

connected = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    connected[a][b] = 1
    connected[b][a] = 1

visited = [False] * (n + 1)

print(bfs(connected, 1, visited))