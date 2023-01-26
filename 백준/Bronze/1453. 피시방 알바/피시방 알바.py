N = int(input())
Number = list(map(int, input().split()))
tmp =  N - len(set(Number))
print(tmp)