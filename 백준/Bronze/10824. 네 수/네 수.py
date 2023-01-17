a,b,c,d = list(map(str, input().split()))
result = a+b, c+d
result2 = list(map(int, result))
sum = 0
for n in result2:
    sum = n + sum
print(sum)