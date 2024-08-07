import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = sorted(list(set(A)))
for i in A:
    print(bisect_left(B, i), end=' ')