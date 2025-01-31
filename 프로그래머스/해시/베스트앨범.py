def solution(genres, plays):
    answer = []
    dic1 = {} # {장르:[[횟수,인덱스],[횟수,인덱스]]}
    dic2 = {} # {장르:[총합]}

    i = 0
    for g, p in zip(genres, plays):
        if g not in dic1:
            dic1[g] = [[p, i]]
            dic2[g] = p
        else:
            dic1[g].append([p,i])
            dic2[g] += p
        i += 1
    print(dic1)
    dic2_list = sorted(list(dic2.items()), key= lambda x:x[1], reverse=True)
    # print(dic2_list)
    for tup in dic2_list:
        g = tup[0]
        k = sorted(dic1[g], key=lambda x:x[0], reverse=True)
        for i in k[:2]:
            answer.append(i[1])

    return answer



a=["classic", "pop", "classic", "classic", "pop"]
b=[500, 600, 150, 800, 2500]
print(solution(a,b))