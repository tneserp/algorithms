import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 0, 1, 0, 0]
dy = [0, -1, 0, 0, 1, 0]
dz = [0, 0, -1, 0, 0, 1]

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 1:
                q.append((i, j, k))

while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and board[nx][ny][nz] == 0:
            board[nx][ny][nz] = board[x][y][z] + 1
            q.append((nx, ny, nz))

ans = float("-inf")
for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == 0:
                ans = float("inf")
            ans = max(ans, board[i][j][k])

if ans == float("inf"):
    print("-1")
else:
    print(ans - 1)
