tmp = []
for n in range(10):
    tmp.append(int(input()))
    result = sum(tmp) // 10
print(result)
print(max(tmp, key=tmp.count))