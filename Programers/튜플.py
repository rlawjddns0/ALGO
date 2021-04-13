import re







def solution(s):
    answer = []
    s=s[1:len(s)-1]#맨 앞에 { 맨 뒤에 } 제거
    s=s.split('}')# }기준으로 나누기
    print(s)
    #입력 :"{2},{2,1},{2,1,3},{2,1,3,4}"
    #출력: ['{2', ',{2,1', ',{2,1,3', ',{2,1,3,4', '']
    s=s[0:len(s)-1]# 맨 마지막에 아무것도 없는 리스트가 생겨서 그거 제거 ? 왜 생기지?
    num_list = []
    for i in range(len(s)):
        tmp=[]
        s[i]=s[i].replace("{","");#문자열에서 { 없애기
        tmp=s[i].split(',')#만약 문자열에 '23,123' 이렇게 돼있으면 이것도 스플릿헤서 리스트로 반환
        tmp1=[]
        for j in range(len(tmp)):#스플릿한 리스트로 다시 for문
            if tmp[j]=="":continue#이것도 왠지 모르겠는데 공백 리스트가 생겨서 조건 추가
            tmp1.append((int)(tmp[j]))#숫자로 바꿔서 임시 리스트에 붙이기
        num_list.append(tmp1)#임시리스트 다시 결과 리스트에 붙이기 -> 이중리스트
    print(num_list)

    num_list = sorted(num_list, key=len)#리스트 길이로 정렬

    for i in num_list:
        for j in range(len(i)):
            if i[j] not in answer:#answr리스트에 i[j] 값이 없으면 
                answer.append(i[j])# 붙이기


    print(answer)


    return answer

