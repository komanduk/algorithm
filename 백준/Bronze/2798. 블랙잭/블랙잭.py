a, b = map(int, input().split())
tmp = list(map(int, input().split()))
result = 0
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            if tmp[i]+tmp[j]+tmp[k] > b:
                pass
            else:
                result = max(result, tmp[i]+tmp[j]+tmp[k])
print(result)