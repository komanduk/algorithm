a = int(input())
x = a
C = 0
while True:
    A = x//10
    b = x%10
    c =(A + b)%10
    x = (b*10) + c
    C +=1
    if x == a:
        print(C)
        break