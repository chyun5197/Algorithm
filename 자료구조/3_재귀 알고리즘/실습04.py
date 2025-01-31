''' 코드업 1920번
2진수 변환
bin(10):
    print(1)
    print(0)
    print(1)
    print(0)
end 옵션 필요
'''
def bin(n):
    if n > 1:
        bin(n//2)
    print(n%2, end='') # 0,1은 그대로 출력

n = int(input())
bin(n)
'''
bin(10): bin(5) 이후 print(0)  
bin(5): bin(2) 이후 print(1)
bin(2): bin(1) 이후 print(0)
bin(1): print(1)  
'''



