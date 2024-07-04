from collections import deque

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

painting = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
size = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    global size
    temp = 1
    queue = deque()
    queue.append((i, j))
    painting[i][j] = 0
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and painting[nx][ny]:
                painting[nx][ny] = 0
                queue.append((nx, ny))
                temp += 1

    size = max(size, temp)


for i in range(n):
    for j in range(m):
        if painting[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)
print(size)
