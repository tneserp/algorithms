from collections import deque
import sys

input = sys.stdin.readline

n, w, L = map(int, input().split())
# 트럭의 수 n, 다리의 길이 w, 다리의 최대하중 L
bus = deque(map(int, input().split()))
bridge = deque(0 for _ in range(w))
cnt = 0

while True:
    if len(bus) == 0 and sum(bridge) == 0:
        break
    bridge.popleft()
    if len(bus) > 0:
        if sum(bridge) + bus[0] <= L:
            bridge.append(bus.popleft())
        else:
            bridge.append(0)
    cnt += 1

print(cnt)
