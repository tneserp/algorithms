# BFS
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(n):
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        j = q.popleft()
        for k in graph[j]:
            if not visited[k]:
                visited[k] = 1
                q.append(k)


ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)
