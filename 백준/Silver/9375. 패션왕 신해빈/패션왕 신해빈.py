import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    ans = 1
    item = {}
    for _ in range(n):
        a, b = input().split()

        if b in item:
            item[b].append(a)
        else:
            item[b] = [a]

    for i in item:
        ans *= (len(item[i]) + 1)

    ans -= 1
    print(ans)
