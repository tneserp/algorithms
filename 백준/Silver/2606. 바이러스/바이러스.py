import sys
from collections import deque

input = sys.stdin.readline

V = int(input().strip())
E = int(input().strip())

graph = [[] for _ in range(V + 1)]
visited = [0] * (V + 1)


def bfs(n):
    q = deque([1])
    cnt = 0
    while q:
        x = q.popleft()
        visited[x] = 1

        for nx in graph[x]:
            if not visited[nx]:
                cnt += 1
                visited[nx] = 1
                q.append(nx)

    return cnt


for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
