import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]


def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


# 지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때,
# 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
# 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며,
# 칸에 쓰여 있는 수는 0이 된다.

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
for i in order:
    if i == 1 and y + 1 < M:
        y += 1
        turn(i)
    elif i == 2 and y - 1 >= 0:
        y -= 1
        turn(i)
    elif i == 3 and x - 1 >= 0:
        x -= 1
        turn(i)
    elif i == 4 and x + 1 < N:
        x += 1
        turn(i)
    else:
        continue

    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0

    print(dice[0])
