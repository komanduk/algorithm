T = int(input())
for t in range(1, T+1):
    n = list(map(int, input().split()))
    print(f'#{t} {max(n)}')