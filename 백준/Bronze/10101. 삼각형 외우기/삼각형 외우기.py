tmp = []
for n in range(3):
    Number = int(input())
    tmp.append(Number)
    sum_ = sum(tmp)
for i in tmp:
    if sum_ != 180:
        print('Error')
    elif tmp.count(60) == 3:
        print('Equilateral')
    elif len(set(tmp)) == 2:
        print('Isosceles')
    else:
        print('Scalene')
    break