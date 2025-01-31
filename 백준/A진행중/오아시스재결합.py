n = int(input())
k = [int(input()) for i in range(n)]
count = n-1
for i in range(n-1):
    for j in range(i+2, n):
        a, b = k[i], k[j]
        isWatch = True
        for h in range(i+1, j):
            if k[h]>min(a,b):
                isWatch = False
                break
        if isWatch:
            count += 1
print(count)