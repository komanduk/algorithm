from collections import deque
N = int(input())
tmp = deque(range(1, N+1))
while len(tmp)>1:
    print(tmp.popleft(), end=" ")
    tmp.append(tmp.popleft())
print(tmp[0])