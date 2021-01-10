#상하좌우
#n*n 크기 1,1에서 시작하여 입력대로 움직이고 최종 목적지 출력
#n*n을 벗어날 수 없음

n=int(input()) # n*n의 크기 입력 받기

direction=list(map(str,input().split()))
x=1
y=1
for i in range(len(direction)):
    if direction[i]=="R":
        if y+1>n:
           y=y
        else:
            y+=1
    elif direction[i]=="L":
        if y-1<1:
            y=y
        else:
            y-=1
    elif direction[i]=="D":
        if x+1>n:
            x=x
        else:
            x+=1
    elif direction[i]=="U":
        if x-1<1:
            x=x
        else:
            x-=1
    else:
        print("error")


print(x,y)

