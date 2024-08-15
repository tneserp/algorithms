import sys
import math

input = sys.stdin.readline

prime = [1] * 246913
prime[1] = False

for i in range(2, math.isqrt(246913)):
    if prime[i]:
        for j in range(2 * i, 246913, i):
            prime[j] = False

while True:
    n = int(input().strip())
    if n == 0:
        break
    ans = 0
    for i in range(n + 1, 2*n+1):
        if prime[i] == 1:
            ans +=1
    print(ans)