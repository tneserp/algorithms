import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(a, b, M, N):
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny]:
                q.append((nx, ny))
                arr[nx][ny] = 0

    return 1


for _ in range(T):
    M, N, K = map(int, input().split())
    ans = 0

    arr = [[0 for _ in range(N)] for _ in range(M)]

    for _ in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1

    q = deque()

    for i in range(M):
        for j in range(N):

            if arr[i][j] == 1:
                bfs(i, j, M, N)
                ans += 1

    print(ans)
