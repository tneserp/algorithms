import sys

input = sys.stdin.readline

str = list(input().strip())

lst = []
ans = 0
val = 1

for i in range(len(str)):
    if str[i] == "(":
        lst.append(str[i])
        val *= 2

    elif str[i] == "[":
        lst.append(str[i])
        val *= 3

    elif str[i] == ")":
        if not lst or lst[-1] == "[":
            ans = 0
            break
        if str[i - 1] == "(":
            ans += val
        lst.pop()
        val //= 2
    else:
        if not lst or lst[-1] == "(":
            ans = 0
            break
        if str[i - 1] == "[":
            ans += val

        lst.pop()
        val //= 3

if lst:
    print(0)

else:
    print(ans)
