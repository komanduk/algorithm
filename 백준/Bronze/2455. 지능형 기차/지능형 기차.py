tmp = {}
total = 0
for i in range(1, 5):
    out_, in_ = map(int, input().split())
    total_ = in_ - out_
    total += total_
    tmp[i] = total
print(max(tmp.values()))