T = int(input())
for t in range(1, T+1):
    money = int(input())
    Quarter, tmp1 = money//25, money%25
    Dime, tmp2 = tmp1//10, tmp1%10
    Nickel, tmp3 = tmp2//5, tmp2%5
    Penny = tmp3//1
    print(Quarter, Dime, Nickel, Penny)