'''
# 우선순위큐
우선수위가 가장 높은 데이터를 가장 먼제 삭제하는 자료구조
힙 사용 - 최소 힙 / 최대 힙

우선순위큐 구현방식   삽입시간    삭제시간
    리스트         O(1)     O(N)
    힙            O(logN)  O(logN)
'''
import heapq # 기본제공은 최소힙

# 오름차순 힙 정렬
def heapsort(iterable):
    h = []
    result = []
    for value in iterable: # 모든 원소를 차례대로 힙에 삽입
        heapq.heappush(h, value)
        # heapq.heappush(h, -value) # @최대힙으로 넣고 싶을때
    for i in range(len(h)): # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
        result.append(heapq.heappop(h))
        # result.append(-heapq.heappop(h)) # @최대힙으로 넣고 싶을때
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
print('='*30)