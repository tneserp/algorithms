from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(N)]

# 초기값 세팅
cloud = deque()
cloud.append([N - 1, 0])
cloud.append([N - 1, 1])
cloud.append([N - 2, 0])
cloud.append([N - 2, 1])


def copyWater(x, y):
    cnt = 0
    if x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] != 0:
        cnt += 1
    if x - 1 >= 0 and y + 1 < N and board[x - 1][y + 1] != 0:
        cnt += 1
    if x + 1 < N and y - 1 >= 0 and board[x + 1][y - 1] != 0:
        cnt += 1
    if x + 1 < N and y + 1 < N and board[x + 1][y + 1] != 0:
        cnt += 1

    return cnt


# 방향에 따른 좌표값 수정
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for d, s in info:
    temp = deque()
    for x, y in cloud:
        nx = (x + dx[d] * s) % N
        ny = (y + dy[d] * s) % N
        temp.append((nx, ny))
        visited[nx][ny] = 1
    cloud = temp

    # 비 내림
    for a, b in cloud:
        board[a][b] += 1

    # 구름이 모두 사라짐
    while cloud:
        a, b = cloud.popleft()
        # 이 때 사라진 구름은 5에서 구름이 생기면 안되기 때문에 visited에 저장
        visited[a][b] = 1

    # 물복사버그 마법 시전
    for a in range(N):
        for b in range(N):
            if visited[a][b]:
                board[a][b] += copyWater(a, b)

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
    for a in range(N):
        for b in range(N):
            if board[a][b] >= 2 and not visited[a][b]:
                cloud.append([a, b])
                board[a][b] -= 2

    # 구름 정보 초기화
    visited = [[0] * N for _ in range(N)]

ans = 0

for a in range(N):
    for b in range(N):
        ans += board[a][b]

print(ans)
