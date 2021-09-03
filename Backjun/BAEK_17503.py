import sys
def binary_search(left,right):
    global N,M,K
    middle=0
    sum=0
    cnt=0
    ans=-1
    while left<=right:
        middle=(left+right)//2
        cnt=0
        sum=0
        # print(middle)
        for i in range(K):
            if beer[i][1]<=middle:
                sum+=beer[i][0]#선호도 합
                cnt+=1#며칠 먹었는지
            if cnt==N: break#N일 먹었으면 빠져나옴
        if cnt!=N or sum<M:#N일을 다 못먹었거나 선호도가 다 안찼으면
            # print("sival",middle)
            left=middle+1#간 레벨을 올린다
        else:#아니면
            right=middle-1
            ans = middle

    print(ans)


N,M,K=map(int,input().split())
beer=[]
max_alch=0
for _ in range(K):
    taste,alch=map(int,sys.stdin.readline().split())
    beer.append((taste,alch))
    if max_alch<alch:
        max_alch=alch

#람다로 정렬 시키기, 0번째가 정렬 조건이 된다.
beer.sort(key=lambda x:x[0],reverse=True)
# print(beer)
binary_search(0,max_alch)

