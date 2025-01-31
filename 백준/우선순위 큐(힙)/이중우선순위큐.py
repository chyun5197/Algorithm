import sys
import heapq
input = sys.stdin.readline
t = int(input())
for i in range(t):
    k = int(input())
    minQ = []
    maxQ = []
    delete = [False] * k # 삭제 여부
    for j in range(k):
        a, b = input().split()
        b = int(b)
        if a=='I': # 삽입
            heapq.heappush(minQ, (b,j))
            heapq.heappush(maxQ, (-b,j))
        else:
            if b == 1: # 최대값 삭제
                while maxQ and delete[maxQ[0][1]]: # 이전 최소값의 삭제부터 반영
                    heapq.heappop(maxQ)
                if maxQ:
                    v, index = heapq.heappop(maxQ)
                    delete[index] = True
            else: # 최소값 삭제
                while minQ and delete[minQ[0][1]]: # 이전 최대값의 삭제부터 반영
                    heapq.heappop(minQ)
                if minQ:
                    v, index = heapq.heappop(minQ)
                    delete[index] = True
        # print('j번 minQ:', minQ)
        # print('j번 maxQ:', maxQ)

    # 최대힙, 최소힙 동기화
    while maxQ and delete[maxQ[0][1]]:
        heapq.heappop(maxQ)
    while minQ and delete[minQ[0][1]]:
        heapq.heappop(minQ)
    # print(delete)
    # print(minQ)
    # print(maxQ)
    # print()

    print(-maxQ[0][0], minQ[0][0]) if minQ else print('EMPTY')


