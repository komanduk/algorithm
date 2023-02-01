T = int(input())
for t in range(T):
    scr = list(map(int, input().split()))
    scr.remove(max(scr))
    scr.remove(min(scr))
    if max(scr) - min(scr) >= 4:
        print('KIN')
    else:
        print(sum(scr))