dic = {}
N = int(input())
for n in range(N):
    name = input().split()
    dic[name[0]] = name[1]
dic_sort = sorted(dic.items(), reverse=True)
for key, value in dic_sort:
    if 'enter' in value:
        print(key)