N = int(input())
sum = 0
for n in range(N):
    cute = int(input())
    sum = cute + sum
if sum > N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")