import sys
from bisect import bisect_left, bisect_right
from itertools import combinations

nA, nB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = list(sorted(set(A) - set(B)))

if len(result):
    print(len(result))
    for i in result:
        print(i, end=' ')
else:
    print(0)
