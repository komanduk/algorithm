from collections import deque
tmp = []
for n in range(int(input())):
    Number = int(input())
    if Number == 0:
        tmp.pop()
    else:
        tmp.append(Number)
print(sum(tmp))