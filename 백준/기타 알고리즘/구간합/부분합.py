import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

# result = []
min = int(1e9)
intervalSum = 0
end = 0
for start in range(n): # start를 차례대로 증가시키며 반복
    while intervalSum < m and end < n: # end부터 움직임
        intervalSum += data[end]
        end += 1
    if intervalSum >= m:
        # result.append(data[start:end])
        length = end-start
        if min > length:
            min = length
    intervalSum -= data[start]
# print(result)
if min!=int(1e9):
    print(min)
else:
    print(0)