import sys

N = int(input())
tmp = []
for n in range(N):
    tmp.append(sys.stdin.readline().strip())
tmpset = set(tmp)
tmp = list(tmpset)
tmp.sort()
tmp.sort(key= len)
for i in tmp:
    print(i)