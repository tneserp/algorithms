import sys

input = sys.stdin.readline

ans = 0

s = input().rstrip()
stick = list()
for i in range(len(s)):
    if s[i] == '(':
        stick.append(s[i])
    elif s[i] == ')':
        stick.pop()
        if s[i - 1] == '(':
            ans += len(stick)
        elif s[i-1] == ')' :
            ans += 1

print(ans)