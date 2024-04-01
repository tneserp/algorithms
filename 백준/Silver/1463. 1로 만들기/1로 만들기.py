import sys

input = sys.stdin.readline

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

d = [float("inf")] * 10000000
d[1] = 0

N = int(input().strip())

for i in range(1, N + 1):
    if i == N + 1:
        break
    if d[i * 3] > d[i] + 1:
        d[i * 3] = d[i] + 1

    if d[i * 2] > d[i] + 1:
        d[i * 2] = d[i] + 1

    if d[i + 1] > d[i] + 1:
        d[i + 1] = d[i] + 1

print(d[N])
