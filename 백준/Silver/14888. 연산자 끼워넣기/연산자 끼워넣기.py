import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
val = list(map(int, input().split()))

operations = list('+' * val[0] + '-' * val[1] + '*' * val[2] + '/' * val[3])

max_num = -2e9
min_num = 2e9

for op in (set(permutations(operations, N - 1))):
    val = A[0]
    for i in range(len(op)):
        if op[i] == '+':
            val += A[i + 1]
        elif op[i] == '-':
            val -= A[i + 1]
        elif op[i] == '*':
            val *= A[i + 1]
        elif op[i] == '/':
            val = int(val / A[i + 1])
    if max_num < val:
        max_num = val
    if min_num > val:
        min_num = val

print(max_num)
print(min_num)