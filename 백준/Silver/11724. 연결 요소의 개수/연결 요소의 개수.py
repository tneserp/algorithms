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

ans = 0

for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = 1
        q = deque([i])
        ans += 1
        while q:
            k = q.popleft()
            for j in graph[k]:
                if not visited[j]:
                    visited[j] = 1
                    q.append(j)

print(ans)
