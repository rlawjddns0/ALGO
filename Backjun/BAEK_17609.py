

def solution(str):
    left=False;
    right=False
    for i in range(len(str)//2):
        if(str[i]!=str[len(str)-1-i]):
            # print(str[i])
            # print(str[len(str)-1-i])
            for j in range(i,len(str)//2):
                # print(str[j+1]+" "+str[len(str)-1-j])
                if str[j+1]!=str[len(str)-1-j]:
                    left=True


            for j in range(i,(len(str)//2)):
                # print(str[j] + " " + str[len(str) - 1 - j-1])
                if(str[j]!=str[len(str)-1-j-1]):
                    right=True


            if left and right:
                return 2
            elif left or right:
                return 1
    return 0


TC = int(input())
for i in range(0,TC):
    str = list(input())
    print(solution(str))


