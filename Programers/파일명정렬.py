import operator
files=  ["abc000123"]

def solution(files):
    answer=[]
    tmp={}
    ans=[]
    num=0
    for i in files:
        num=num+1
        tmp[num]=i.lower()#dictionary로 바꾸기 1:"asdf12.gif"
    n=1
    for i in tmp:

        head=HEAD(tmp[i])#머리 떼오기
        num=NUM(tmp[i])#숫자 뗴오기
        tail=TAIL(tmp[i])#꼬리 떼오기
        h={"order": n, "head":head,"num":num,"tail":tail}# index도 함께 머리 숫자 꼬리 저장
        ans.append(h)#리스트에 붙이기
        n=n+1




    #print(ans)
    new_list=sorted(ans, key=operator.itemgetter('head','num') )#head->num 순서로 정렬 후 list로 반환
    #print(new_list)
    #new_list = sorted(new_list, key=operator.itemgetter('num'))
    #print(new_list)
    for i in range(len(new_list)):
        answer.append(files[new_list[i].get('order')-1])#저장해놨던 index를 사용하여 files리스트 가져옴
    print(answer)
    return answer
def HEAD(str):
    head=0

    for i in range(len(str)):
        if str[i].isdigit() :#머리에는 무조건 문자로만 이어져있으니까 숫자 나오면 break
            head=i
            break
    return str[:head]#숫자 전까지가 다 머리

def NUM(str):
    start=0
    end=0
    for i in range(len(str)):
        if str[i].isdigit():#숫자가 시작되면
            start=i
            tmp=i
            while(tmp<len(str)):
                if str[tmp].isalpha():#다시 숫자가 아닌게 나올때까지 반복하다가 나오면
                    end=tmp-1#하나 빼줌
                    break
                else:#아니면 인덱스 +1
                    end=tmp+1
                    tmp=tmp+1
            break

    return int(str[start:end])#000123 이렇게 나와도 int형으로 바꾸면 123으로 바꿔줌

def TAIL(str):
    tmpn=0
    flag=False
    i=0
    for i in range(len(str)-1):
        if str[i].isdigit():#숫자가 나오면
            #print(i)
            if (str[i+1]).isdigit()==False:#숫자 다음에 자리에서 숫자가 아닌게 나오면
                tmpn=i#그 인덱스 기억
                flag=True
                break

    if flag==True:#저장한 인덱스 +1 부터 뒤에가 다 꼬리
        return str[tmpn+1:]

    return#꼬리가 없는경우

solution(files)


