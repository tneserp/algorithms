import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
ans = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r - 1][c - 1] = [s, d, z]

# 1. 낚시왕이 오른쪽으로 한 칸 이동한다.
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 3. 상어가 이동한다.

# 각 이동 방향에 대한 dx, dy
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for fishingKing in range(C):
    copyBoard = [[0] * C for _ in range(R)]

    # 땅과 제일 가까운 상어를 잡는다.
    for i in range(R):
        if board[i][fishingKing] != 0:
            ans += board[i][fishingKing][2]
            board[i][fishingKing] = 0
            break

    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                s, d, z = board[i][j]

                # 상어의 이동 방향에 따른 이동 거리 계산
                if d == 1 or d == 2:
                    s %= (2 * (R - 1))
                else:
                    s %= (2 * (C - 1))

                # 상어 이동
                nx, ny = i, j
                for _ in range(s):
                    if (nx == 0 and d == 1) or (nx == R - 1 and d == 2):
                        d = 1 if d == 2 else 2
                    if (ny == 0 and d == 4) or (ny == C - 1 and d == 3):
                        d = 3 if d == 4 else 4

                    nx += dx[d - 1]
                    ny += dy[d - 1]

                # 이동한 위치에 상어 배치 (크기가 큰 상어가 들어감)
                if copyBoard[nx][ny] == 0 or copyBoard[nx][ny][2] < z:
                    copyBoard[nx][ny] = [s, d, z]

    board = copyBoard

print(ans)
