import sys

input = sys.stdin.readline

N = int(input().strip())

RGB = [list(map(int, input().split())) for _ in range(N)]

D = [[0, 0, 0] for _ in range(N + 1)]

# D[k][0] = 빨강색으로 칠했을 때
# D[k][1] = 초록색으로 칠했을 때
# D[k][2] = 파랑색으로 칠했을 때

D[1][0] = RGB[0][0]
D[1][1] = RGB[0][1]
D[1][2] = RGB[0][2]

for i in range(2, N + 1):
    D[i][0] = min(D[i - 1][1], D[i - 1][2]) + RGB[i - 1][0]
    D[i][1] = min(D[i - 1][0], D[i - 1][2]) + RGB[i - 1][1]
    D[i][2] = min(D[i - 1][0], D[i - 1][1]) + RGB[i - 1][2]

print(min(D[N][0], D[N][1], D[N][2]))
