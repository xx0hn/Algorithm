# 문제
# 크기가 3×3인 배열 A가 있다. 배열의 인덱스는 1부터 시작한다. 1초가 지날때마다 배열에 연산이 적용된다.
#
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다. 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.
#
# 예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.
#
# 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 달라질 수 있다. R 연산이 적용된 경우에는 가장 큰 행을 기준으로 모든 행의 크기가 변하고, C 연산이 적용된 경우에는 가장 큰 열을 기준으로 모든 열의 크기가 변한다. 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다. 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.
#
# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
#
# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.
#
# 입력
# 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
#
# 둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.
#
# 출력
# A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 100초가 지나도 A[r][c] = k가 되지 않으면 -1을 출력한다.
from collections import defaultdict
r, c, k=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(3)]
r, c=r-1, c-1
answer=0
def cul_r():
    lst=[]
    for i in range(len(a)):
        d = defaultdict(int)
        for j in range(len(a[0])):
            if a[i][j]==0:
                continue
            d[a[i][j]]+=1
        result=[]
        for key, value in d.items():
            result.append((key, value))
        result.sort(key=lambda x: (x[1], x[0]))
        tmp=[]
        for x, y in result:
            tmp+=[x, y]
        lst.append(tmp)
    mx_l=0
    for i in range(len(lst)):
        mx_l=max(mx_l, len(lst[i]))
    for i in range(len(lst)):
        lst[i]+=[0]*(mx_l-len(lst[i]))
        if len(lst[i])>100:
            lst[i]=lst[i][:100]
    return lst
def cul_c():
    lst=[]
    for i in range(len(a[0])):
        d = defaultdict(int)
        for j in range(len(a)):
            if a[j][i]==0:
                continue
            d[a[j][i]]+=1
        result=[]
        for key, value in d.items():
            result.append((key, value))
        result.sort(key=lambda x: (x[1], x[0]))
        tmp=[]
        for x, y in result:
            tmp += [x, y]
        lst.append(tmp)
    mx_l = 0
    for i in range(len(lst)):
        mx_l = max(mx_l, len(lst[i]))
    for i in range(len(lst)):
        lst[i]+=[0]*(mx_l-len(lst[i]))
        if len(lst[i])>100:
            lst[i]=lst[i][:100]
    r_lst=[[0 for _ in range(len(lst))] for _ in range(len(lst[0]))]
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            r_lst[j][i]=lst[i][j]
    return r_lst
while True:
    if len(a)>r and len(a[0])>c:
        if a[r][c]==k:
            break
    if answer>=100:
        answer=-1
        break
    if len(a)>=len(a[0]):
        a=cul_r()
    else:
        a=cul_c()
    answer+=1
print(answer)
