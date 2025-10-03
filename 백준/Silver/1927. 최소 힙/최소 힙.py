import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

heap = []
heapq.heapify(heap)

for _ in range(N):
    x = int(input().strip())

    if x == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
