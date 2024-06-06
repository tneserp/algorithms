from itertools import combinations
import sys

input = sys.stdin.readline

N = int(input().strip())

S = [list(map(int, input().split())) for _ in range(N)]

person = [i for i in range(N)]
ans = float("inf")

for team in combinations(person, N // 2):
    startTeam = 0
    linkTeam = 0

    for i, j in combinations(team, 2):
        startTeam += (S[i][j] + S[j][i])

    for i, j in combinations(set(person) - set(team), 2):
        linkTeam += (S[i][j] + S[j][i])
    ans = min(ans, abs(startTeam - linkTeam))

print(ans)
