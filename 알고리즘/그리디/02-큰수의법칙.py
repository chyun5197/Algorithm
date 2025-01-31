# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
n = 5
m = 8
k = 3
a = [2,4,5,4,6] #[3,4,3,4,3]
mp = {}
for i in a:
    if i not in mp:
        mp[i] = 1
    else:
        mp[i] += 1

dsc = sorted(list(mp.keys()), reverse=True)
m1 = dsc[0]
m2 = dsc[1]
cnt = 0
num = 0

if mp[m1] > 1:
    num += mp[m1]*m*2
else:
    for i in range(m):
        if cnt < k: # cnt 안쓰고 m을 -1씩 줄이면 변수하나 아낌.
            num += m1
            cnt+=1
        else:
            num += m2
            cnt = 0
print(num)

###################
# 수열로 풀기(답안)
a.sort()
first = a[n-1]
second = a[n-2] # 중복포함

cnt = int(m/(k+1)) * k
cnt += m%(k+1)
ret = 0
ret += cnt*first
ret += (m-cnt)*second
print(ret)
