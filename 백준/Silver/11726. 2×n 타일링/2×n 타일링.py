import sys

input = sys.stdin.readline

N = int(input().strip())

D = [0] * 1005
D[1] = 1
D[2] = 2

if N < 3:
    print(D[N])
    sys.exit()

for i in range(3, N + 1):
    D[i] = D[i - 2] + D[i - 1]

print(D[N] % 10007)
