n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:
        ns = list(map(int, str(i)))#숫자를 자리수대로 분리
        if ns[0] - ns[1] == ns[1] - ns[2]:
            han += 1
print(han)