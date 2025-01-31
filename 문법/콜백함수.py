'''
# 콜백 함수(Callback Function)란?
직접 호출하는 것이 아닌 다른 함수에 의해 호출되는 함수
함수 호출 시에 함수를 입력 인자로 전달하고 호출받은 함수에서는 전달받은 함수를 호출하여 사용
'''
def main(sub, par):
    sub()
    par(20)

def sub():
    print('서브 함수')

def par(num):
    print(num + 10)

main(sub, par) # 여기서 sub, par가 콜백함수
