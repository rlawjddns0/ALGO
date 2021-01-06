x = int(input())
count = 0
mylist = []
for i in range(x):
    mylist.append(list(map(int, input().split())))

for i in range(x):
    if sum(mylist[i]) > 1:
        count += 1

print(count)