import heapq
import sys

input = sys.stdin.readline

heap = []

N = int(input().strip())

for _ in range(N):
    a = int(input().strip())
    if a != 0:
        heapq.heappush(heap, (abs(a),a))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print("0")