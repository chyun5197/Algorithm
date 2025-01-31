'''
# 쉘 정렬(shell sort)
단순 삽입 정렬의 장점은 살리고 단점은 보완하여 더 빠르게 정렬하는 알고리즘
'''
def shell_sort(a): # O(n^1.25)
    n = len(a)
    h = len(a)//2 # h칸씩 떨어진 원소들끼리 정렬
    while h>0:
        # j가 앞원소 | i가 뒤원소 | a[j] ~ a[i==j+h]
        for i in range(h, n): # 이 for문은 삽입정렬과 같음
            j = i - h # 0번 ~ (n-h)번 인덱스까지 쌍으로 선택
            tmp = a[i] # 맨뒤 원소 킵
            while j>=0 and a[j] > tmp: # 앞원소가 뒤원소보다 크면 교환하면서, 맨뒤원소가 들어갈 위치까지 반복진행
                a[j+h] = a[j] # 바로앞 원소를 바로뒤에 저장하고
                j -= h # 앞쪽 원소들끼리도 비교
            a[j+h] = tmp # 맨뒤원소를 현재의j 위치에 삽입
        h //= 2 # 떨어질 h칸 절반으로 줄임 1까지.
num = int(input("원소 개수 입력: "))
x = [0]*num

for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

shell_sort(x)
print(x)