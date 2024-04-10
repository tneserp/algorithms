import sys

from collections import deque

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)
visited = [0] * (n + 1)


def bfs():
    q = deque([1])
    visited[1] = 1
    ans = 0

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                dist[nx] = dist[x] + 1
                if dist[nx] == 3:
                    return ans
                visited[nx] = 1
                ans += 1
                q.append(nx)

    return ans


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs())
