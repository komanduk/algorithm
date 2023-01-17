T = int(input())
sum_ = 0
for t in range(1, T+1):
    N = int(input())
    Number = list(map(int, input().split()))
    sum_ = 0
    for n in Number: 
        sum_ = n + sum_
    print(sum_)