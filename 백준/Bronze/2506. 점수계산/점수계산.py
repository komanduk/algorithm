N = int(input())
OX = list(map(int, input().split()))
sum = 0
result = 0
for n in range(N):
    if OX[n] == 1:
        sum += 1
        result +=sum
    else:
        sum = 0
print(result)