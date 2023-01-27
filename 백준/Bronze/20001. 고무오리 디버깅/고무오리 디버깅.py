ori_tmp = []
while True:
    ori = input()
    if ori == '문제':
        ori_tmp.append(ori)
    elif ori == '고무오리':
        if ori_tmp:
            ori_tmp.pop()
        else:
            ori_tmp.append('문제')
            ori_tmp.append('문제')
    elif ori == '고무오리 디버깅 끝':
        break
if ori_tmp.count('문제') > 0:
    print('힝구')
else:
    print('고무오리야 사랑해')