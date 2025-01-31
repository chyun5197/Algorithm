# 원형 큐
# 연결리스트
def solution(food_times, k):
    n = len(food_times)
    f = []
    for i in range(n):
        f.append([food_times[i], i+1]) # [개수, 번호]

    idx = 0
    while True:
        if len(f)==0:
            return -1
        if idx == len(f):
            idx = 0
        if f[idx][0] == 0:
            del f[idx]
            continue
        f[idx][0] -= 1
        k -= 1
        answer = f[idx][1]
        if k == 0:
            break

    return answer

print(solution([3, 1, 2], 5))