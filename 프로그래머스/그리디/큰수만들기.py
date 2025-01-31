def solution(number, k):
    answer = ''
    nums = list(map(int, list(number)))
    cnt = 0
    for i in range(len(number)):
        if i == 0:
            if nums[i] < nums[i+1]:
                cnt+=1
        # elif:
        #     pass
        print(f'{i}, {k}: {answer}')

    return answer

# print(solution("1924", 2)) #94
print(solution("1231234", 3)) #3234
# print(solution("4177252841", 4))
