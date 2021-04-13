def check(stones,middle, k):
    count=0
    for i in range(len(stones)):
        if stones[i]<middle:
            count+=1
            if count>=k: return False
        else:
            count=0

    return True;

def solution(stones, k):
    answer = 0
    left=0
    right=max(stones)#가장 큰 징검다리 수가 곧 갈 수 있는 최대 인원의 수

    while left<=right:
        middle=(int)((left+right)/2)

        if check(stones,middle,k):
            answer=max(answer,middle)
            left=middle+1
        else:
            right=middle-1



    return answer
