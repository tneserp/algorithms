import sys

input = sys.stdin.readline


def sum_num(s):
    value = 0
    for i in s:
        if i.isdigit():
            value += int(i)
    return value


N = int(input())
serial = [input().rstrip() for _ in range(N)]
serial.sort(key=lambda x: (len(x), sum_num(x), x))

for i in serial:
    print(i)
