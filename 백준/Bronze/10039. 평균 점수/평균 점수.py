N = 5
sum = 0
for _ in range(N):
    score = int(input())
    if 40 > score:
        score = 40
    sum = score + sum
result = sum//N
print(result)