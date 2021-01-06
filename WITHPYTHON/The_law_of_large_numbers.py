# n,m,k=map(int, input().split())#공백으로 숫자 받기
#
# num_list=list(map(int,input().split()))#공백으로 n개 숫자 받기
#
# num_list.sort()
# first=num_list[-1]
# second=num_list[-2]
# sum=0
#
# while True:
#     for i in range(k):
#         if m==0:
#             break
#         sum+=first
#         m-=1
#     if m==0:
#         break
#     sum+=second
#     m-=1
#
# print(sum)


# 최적화

n,m,k=map(int, input().split())#공백으로 숫자 받기

num_list=list(map(int,input().split()))#공백으로 n개 숫자 받기

num_list.sort()
first=num_list[-1]
second=num_list[-2]

count=m//(k+1)
count+=m%(k+1)

sum=first*k +second

result=count*sum

print(result)