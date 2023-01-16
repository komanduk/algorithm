N, X = map(int, input().split())
Number = list(map(int, input().split()))
for tmp in Number:
    if tmp < X:
        print(tmp, end=' ')