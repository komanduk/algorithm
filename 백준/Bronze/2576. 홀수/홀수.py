s= []
for t in range(7):
    T = int(input())
    if T%2 == 1:
        s.append(T)
if len(s) == 0:
    print(-1)
else:
    print(sum(s))
    print(min(s))