import sys

input = sys.stdin.readline

A = int(input().strip())

num = list(map(int, input().split()))

d = [1 for _ in range(1001)]

for i in range(1, A ):
    for j in range(i):
        if num[i] > num[j]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))