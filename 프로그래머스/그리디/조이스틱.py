
def solution(name):
    spellCnt = 0 # 알파벳 선택
    cursorCnt = 0 # 좌우

    for i, w in enumerate(name):
        spellCnt += min(ord(w)-ord('A'), ord('Z')-ord(w)+1)




    answer = 0


    return answer

# print(solution('JEROEN')) # 56
# print(solution('JAN')) # 23
print(solution('AAAAAAAA')) # 0

