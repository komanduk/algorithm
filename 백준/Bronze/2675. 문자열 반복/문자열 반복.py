T = int(input())
for t in range(1, T+1):
    a, b = input().split()
    A = int(a)
    B = str(b)
    for i in range(len(B)):
        print(A*B[i], end='')
    print()