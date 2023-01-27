a, b = map(int, input().split())
Number1 = list(map(int, input().split()))
Number2 = list(map(int, input().split()))
Number1_tmp = set(Number1)
Number2_tmp = set(Number2)
tmp = Number1_tmp - Number2_tmp
tmp2 = Number2_tmp - Number1_tmp
print(len(tmp)+len(tmp2))