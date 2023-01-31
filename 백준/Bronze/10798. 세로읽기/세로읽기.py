tmp = []
for n in range(5):
    tmp.append(input())
for i in range(15):
    for a in range(5):
        try:
            print(tmp[a][i], end='')
        except:
            pass