import sys

input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    n = int(input().strip())
    fashion = dict()
    for j in range(n):
        a, b = input().split()
        if b not in fashion:
            fashion[b] = 1
        else:
            fashion[b] += 1
    sum = 1
    for i in fashion.values():
        sum *= i + 1
    print(sum - 1)