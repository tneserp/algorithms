import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)


def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if dist[nx] == 0:
                dist[nx] = dist[x] + 1
                q.append(nx)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
ans = 0
for i in range(2, n + 1):
    if 0 < dist[i] <= 2:
        ans += 1
print(ans)
