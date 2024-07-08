import sys

input = sys.stdin.readline

from collections import deque

board = [0] * 100001
N, K = map(int, input().split())
q = deque()
q.append(N)

while q:
    x = q.popleft()
    if x == K:
        break
    for nx in [x - 1, x + 1, x * 2]:
        if 0 <= nx < 100001 and board[nx] == 0:
            board[nx] = board[x] + 1
            q.append(nx)

print(board[K])
