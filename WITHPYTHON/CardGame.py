# 숫자 카드 게임
# 행중에 가장 작은 수 를 구하고 그중에서 큰수를 반환하는 문제

n,m=map(int,input().split())
result=0
for i in range(n):
    data=list(map(int,input().split()))
    MIN=min(data)#리스트 중 가장 작은 값 반환
    result=max(result,MIN)#값을 비교해서 큰 값 찾기

print(result)
