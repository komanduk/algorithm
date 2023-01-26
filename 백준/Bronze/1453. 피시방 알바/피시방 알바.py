N = int(input())
Number = list(map(int, input().split()))
print(N - len(set(Number)))