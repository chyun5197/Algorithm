h = input()
h = [ord(h[0])-96, int(h[1])]
print(h)

move = [[2,1], [1,2], [-1,2], [-2,1], [-1,-2], [-2,-1], [1,-2], [2,-1]]
cnt = 0
for i in range(len(move)):
    k = [move[i][0]+h[0], move[i][1]+h[1]]
    if 1<=k[0]<=8 and 1<=k[1]<=8:
        cnt+=1
print(cnt)