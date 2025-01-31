import sys
input = sys.stdin.readline

from heapq import heappop, heappush
heap = []

n = int(input())
for i in range(n):
    heappush(heap, int(input()))
total = 0
while len(heap)!=1:
    pair = heappop(heap) + heappop(heap)
    total += pair
    heappush(heap, pair)
print(total)