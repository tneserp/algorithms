import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = sorted([int(input().strip()) for _ in range(N)])

start = 0
end = 0
ans = float("inf")

for st in range(start, N):
    while end < N and A[end] - A[st] < M:
        end += 1
    if end == N:
        break
    ans = min(ans, A[end] - A[st])
print(ans)