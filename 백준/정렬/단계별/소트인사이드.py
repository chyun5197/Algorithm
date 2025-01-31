n = input()
msg = [i for i in n]
msg.sort(reverse=True)
k = ''.join(msg)
print(k)