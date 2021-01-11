def solution(n):
    sum=0
    for x in list(str(n)):
        sum+=int(x)
    return int(n)+sum


arr=[]
for i in range(1,10001):
    idx=solution(i)
    arr.append(idx)# 셀프 넘버 아닌거


for i in range(1,10001):
    if i in arr:
        pass
    else:
        print(i)


