n = int(input())
k = list(map(int, input().split()))
k.sort()
cnt = 0

# mine
size = len(k)
for i in range(size):
    if k[i] < size - (i+1):
        cnt += 1
        i += k[i]
print(cnt)

# 답 안
ret = 0 # 총 그룹 수
cnt = 0 # 현재 그룹에 포함된 모험가 수
for i in k:
    cnt += 1 # 현재 그룹에 해당 모험가 추가
    if cnt>=i:# 현재 그룹에 포함된 모험가 수가 현재의 공포도 이상이면, 그룹 결성
        ret+=1
        cnt = 0