import sys
input = sys.stdin.readline
t = int(input())
test = [int(input()) for i in range(t)]
dp = [0] * 1000000
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for i in test:
    print(dp[i])


#
# max_value = max(test)
# from itertools import product
# nums = [0,1,2,3]
# for num in test:
#     case = set()
#     for i in product(nums, repeat = num):
#         if sum(i) == num:
#             msg = ''.join(map(str, i))
#             msg = msg.replace('0', '')
#             case.add(msg)
#     print(len(case))

# case = [0] * (max_value+1) # 1~10까지 만들수 있는 조합 모두 준비
# caseList = [[] for i in range(max_value+1)]  # 1~10까지 만들수 있는 조합 모두 준비
# caseList = []  # 1~10까지 만들수 있는 조합 모두 준비
# case[1] = 1
# case[2] = 2 # (1,1) (2)
# case[3] = 4 # (1,1,1) (1,2) (2,1), (3) = c[1] + c[2] + 1
# case[4] = 7 #
# case[5] =     # (4,1) (3,2) (2,3), (1,4) + [4]
# case[6] =
# case[7] =
# caseList.append([1])
# caseList.append([1,1])
# caseList.append([2])
# caseList.append([1,1,1])
# caseList.append([2,1])
# caseList.append([1,2])
# caseList.append([3])

# n = 4
# while n!=max_value+1:
#     for one in range(n,-1,-1):
#         for two in range(n,-1,-1):
#
#
#     n+=1

# print(caseList[1])
# print(caseList[2])
# print(caseList[3])

# for i in range(4, max_value+1):
#     case = []
#     for lists in combinations(caseList, 2):
#



