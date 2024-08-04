import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]


def dfs(n):
    print(n, end=' ')
    visited[n] = 1
    for nx in graph[n]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)


def bfs(n):
    visited[n] = 1

    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        print(x, end=' ')
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                queue.append(nx)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
visited = [0] * (N + 1)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
