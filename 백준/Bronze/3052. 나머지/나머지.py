a = []
for n in range(10):
    tmp =int(input())
    N_tmp = tmp%42
    a.append(N_tmp)
print(len(set(a)))