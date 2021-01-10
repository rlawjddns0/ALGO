
#1 만들기
#n,k 입력값
# n이 1이 될때 까지수행
#방법 1: n을 k의 배수로 만들기 위해서 n에서 1씩 빼기
#방법 2: n을 k로 나누기
n,k=map(int,input().split())

count=0# 최소 횟수

while(True):
    if n%k!=0:
        n-=1
        count+=1
        if n==1:
            break
    elif n%k==0:
        n=n//k
        count+=1
        if n==1:
            break


print(count)
