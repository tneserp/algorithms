from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps):
    queue = deque()
    queue.append((0, 0))
    n = len(maps[0])
    m = len(maps)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1

    if maps[m - 1][n - 1] == 1:
        return -1
    else:
        return maps[m - 1][n - 1]
