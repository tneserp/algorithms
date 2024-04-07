import sys

input = sys.stdin.readline

N = int(input().strip())
seat = [[0] * N for _ in range(N)]
student = {}

for _ in range(N ** 2):
    temp = list(map(int, input().split()))
    student[temp[0]] = temp[1:]


def getLove(num):
    loveFirst = [[0] * N for _ in range(N)]

    # 1단계
    # 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    hubo1 = []
    temp = float("-inf")
    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0 and i - 1 >= 0 and seat[i - 1][j] in student[num]:
                loveFirst[i][j] += 1
            if seat[i][j] == 0 and i + 1 < N and seat[i + 1][j] in student[num]:
                loveFirst[i][j] += 1
            if seat[i][j] == 0 and j - 1 >= 0 and seat[i][j - 1] in student[num]:
                loveFirst[i][j] += 1
            if seat[i][j] == 0 and j + 1 < N and seat[i][j + 1] in student[num]:
                loveFirst[i][j] += 1

    for i in loveFirst:
        temp = max(temp, max(i))

    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0 and loveFirst[i][j] == temp:
                hubo1.append((i, j))
    if len(hubo1) == 1:
        return hubo1[0]

    # 2단계
    # 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    loveSecond = [[0] * N for _ in range(N)]
    hubo2 = []
    temp = float("-inf")

    for x, y in hubo1:
        if seat[x][y] == 0 and x - 1 >= 0 and seat[x - 1][y] == 0:
            loveSecond[x][y] += 1
        if seat[x][y] == 0 and x + 1 < N and seat[x + 1][y] == 0:
            loveSecond[x][y] += 1
        if seat[x][y] == 0 and y - 1 >= 0 and seat[x][y - 1] == 0:
            loveSecond[x][y] += 1
        if seat[x][y] == 0 and y + 1 < N and seat[x][y + 1] == 0:
            loveSecond[x][y] += 1

    for i in loveSecond:
        temp = max(temp, max(i))

    for i in range(N):
        for j in range(N):
            if seat[i][j] == 0 and loveSecond[i][j] == temp and (i, j) in hubo1:
                hubo2.append([i, j])
    if len(hubo2) == 1:
        return hubo2[0]
    # 3단계
    # 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
    # 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
    hubo2.sort(key=lambda k: (k[0], k[1]))
    return hubo2[0]


def calculateLove(x, y, num):
    love = 0
    if x - 1 >= 0 and seat[x - 1][y] in student[num]:
        love += 1
    if x + 1 < N and seat[x + 1][y] in student[num]:
        love += 1
    if y - 1 >= 0 and seat[x][y - 1] in student[num]:
        love += 1
    if y + 1 < N and seat[x][y + 1] in student[num]:
        love += 1
    return love


ans = 0

for i in student:
    temp = getLove(i)
    seat[temp[0]][temp[1]] = i

for i in range(N):
    for j in range(N):
        ans += (10 ** (calculateLove(i, j, seat[i][j])))//10

print(ans)
