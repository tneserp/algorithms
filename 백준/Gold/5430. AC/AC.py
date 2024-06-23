from collections import deque
import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    flag = 0
    check = 0
    index = 0
    p = input().strip()
    n = int(input().strip())
    a = input().strip().replace('[', '').replace(']', '').split(',')
    num = deque()
    for i in a:
        if '0' <= i <= '99':
            num.append(i)
    for i in p:
        if i == 'D':
            if len(num) == 0:
                flag = 1
                break
            else:
                if check:
                    num.pop()
                else:
                    num.popleft()
        elif i == 'R':
            if check:
                check = 0
            else:
                check = 1
    if flag == 1:
        print("error")
        continue
    else:
        if check:
            num.reverse()
    print('[', end='')
    for i in num:
        if index == len(num) - 1:
            print(i, end='')
        else:
            print(i, end=',')
            index += 1
    print(']')