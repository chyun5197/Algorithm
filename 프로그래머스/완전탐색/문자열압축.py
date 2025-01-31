def solution(s):
    n = len(s)
    if n==1:
        return 1
    h = n//2 # 절반
    compList = []
    unit = 1
    while unit<=h: # 단위가 1~절반 일때
        idx = 0 # 비교 시작 index
        first = s[idx:idx+unit] # 첫값
        a = idx + unit
        # next = s[a:a+unit] # 비교대상
        comp = '' # 압축된 문자열
        while idx<n-unit: # 첫값 설정을 처음부터 끝까지
            cnt = 1 # 같은 문자열 개수
            while True: # 첫값과 다른게 나올때까지 비교
                if s.check(first, a) == a:
                    cnt += 1
                    a += unit
                else:
                    a+=unit
                    comp += first if cnt==1 else str(cnt)+first
                    # if cnt == 1:
                    #     comp += first
                    # else:
                    #     comp += str(cnt) + first
                    break
                # if first==next: # 같으면
                #     cnt += 1
                #     a += unit # 다음 탐색으로 넘어감
                #     next = s[a:a + unit]  # 비교대상
                # else: # 첫값과 다르면 종료
                #     a += unit # 다음 탐색으로 넘어감
                #     next = s[a:a + unit]  # 비교대상
                #     if cnt == 1:
                #         comp += first
                #     else:
                #         comp += str(cnt) + first
                #     break
            idx += cnt*unit # 다음 탐색지점
            first = s[idx:idx + unit]  # 첫값
            # print(comp)
        comp += s[idx:] # 남은 문자열 추가
        unit+=1
        # compList.append(comp)
        compList.append(len(comp))
    # print(compList)
    return min(compList)

msg = 'aabbaccc'
# msg = 'ababcdcdababcdcd'
# msg = 'abcabcdede'
# msg = 'abcabcabcabcdededededede'
# msg = 'xababcdcdababcdcd'
print(solution(msg))
