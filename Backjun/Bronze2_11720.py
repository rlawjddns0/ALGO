num=int(input())
number=int(input())
sum=0
while(True):
    if num==0:
        break
    a = 10 ** (num-1)
    sum+=number//a
    number=number-(number//a)*a
    num-=1

print(sum)
