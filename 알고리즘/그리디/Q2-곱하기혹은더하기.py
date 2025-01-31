s = input()
ret = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    if num <=1 or ret <= 1:
    # if num==0 or num==1 or ret == 0:
        ret+=num
    else:
        ret*=num
print(ret)