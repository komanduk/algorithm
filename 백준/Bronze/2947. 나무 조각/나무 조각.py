T = list(map(int, input().split()))
while True:
    for i in range(len(T)-1):
        if T[i] > T[i +1]:
            T[i], T[i +1] = T[i +1], T[i]
            print(' '.join(map(str, T)))
    if [1, 2, 3, 4, 5] == T:
        break