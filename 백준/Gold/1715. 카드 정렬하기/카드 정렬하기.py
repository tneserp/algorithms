import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
heap = []

for i in range(N):
    heapq.heappush(heap,int(input().strip()))

sum = 0
while len(heap) != 1:
    temp = heapq.heappop(heap) + heapq.heappop(heap)
    sum += temp
    heapq.heappush(heap, temp)

print(sum)