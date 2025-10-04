import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

campus = [list(input().strip()) for _ in range(N)]
dist = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
ans = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            q.append((i, j))
            dist[i][j] = 1
while q:

    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X' and not dist[nx][ny]:
            if campus[nx][ny] == 'P':
                ans += 1
            dist[nx][ny] = 1
            q.append((nx, ny))

if ans:
    print(ans)
else:
    print('TT')
