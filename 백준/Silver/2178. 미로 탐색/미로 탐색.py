from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().strip())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))


bfs()
print(board[N - 1][M - 1])
