T = int(input())
for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    tmp = a // b
    tmp_ = a % b
    print(f'#{t} {tmp} {tmp_}')