'''
# 투 포인터
- '특정한 합을 가지는 부분 연속 수열 찾기' 문제에서 유용
- 수행시간을 줄이기위함. 완전탐색O(n^2) -> 투포인터O(n)
알고리즘 과정
1) start와 end가 첫 번째 원소의 인덱스(0)를 가리키도록 한다.
2) 현재 부분 합이 M과 같다면, 카운트한다
3) 현재 부분 합이 M보다 작다면, end를 1 증가시킨다 (부분합 증가시킴)
4) 현재 부분 합이 M보다 크거나 같다면, start를 1증가시킨다
5) 모든 경우를 확인할때까지 2)~4)과정 반복
문제마다 효율적인 알고리즘 코드 달라질 수 있음
'''
# 1. 부분합을 만족하는 개수 찾기 - [start:end]임
n = 5 # 데이터의 개수 N
m = 5 # 찾으려는 부분합 M
data = [1,2,3,2,5] # 전체 수열

cnt = 0
intervalSum = 0
end = 0
for start in range(n): # start를 차례대로 증가시키며 반복
    while intervalSum < m and end < n: # end부터 움직임
        intervalSum += data[end]
        end += 1
    if intervalSum == m:
        cnt+=1
    intervalSum -= data[start]
print(cnt)

# 2. 정렬되어 있는 두 리스트를 합집합하기
n,m =3,4
a = [1,3,5] # 사전 정렬된 두 리스트
b = [2,4,6,8]
result = [0] * (n+m) # 리스트 a와 b만큼의 개수로 초기화
i,j,k = 0,0,0
while i<n or j<m: # 모든 원소가 결과 리스트에 담길 때까지 반복
    # 리스트 B의 모든 원소가 처리되었거나, 리스트 A의 원소가 더 작을 때
    if j>=m or (i<n and a[i]<=b[j]):
        result[k] = a[i] # 리스트 A의 원소를 결과 리스트로 옮기기
        i += 1
    else: # 리스트A의 모든 원소가 처리되었거나(i>=n), 리스트 B의 원소가 더 작을때(a[i]>b[j])
        result[k] = b[j] # 리스트 B의 원소를 결과 리스트로 옮기기
        j += 1
    k += 1
# 결과 리스트 출력
print(*result, sep=' ')


