import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        temp = q.popleft()
        print(temp, end=" ")
        for k in graph[temp]:
            if not visited[k]:
                visited[k] = 1
                q.append(k)
    print()

# 재귀 DFS
def dfs(n):
    print(n, end=" ")
    visited[n] = 1
    for k in graph[n]:
        if not visited[k]:
            dfs(k)


graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(V)
visited = [0] * (N + 1)
print()
bfs(V)
