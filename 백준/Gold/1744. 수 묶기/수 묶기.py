import sys

input = sys.stdin.readline

N = int(input().strip())
num = sorted([int(input().strip()) for _ in range(N)])

ans = 0
while num:
    if len(num) == 1:
        ans += num[0]
        break
    if num[-1] <= 0:
        num.sort(reverse=True)
    if num[-1] * num[-2] > num[-1] + num[-2]:
        a = num.pop()
        b = num.pop()
        ans += a * b
    else:
        ans += num.pop()

print(ans)
