# 문제
# 재현시의 시장 구재현은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진 구재현은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 재현시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고 한다.
#
# 재현시는 크기가 N×N인 격자로 나타낼 수 있다. 격자의 각 칸은 구역을 의미하고, r행 c열에 있는 구역은 (r, c)로 나타낼 수 있다. 구역을 다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.
#
# 선거구를 나누는 방법은 다음과 같다.
#
# 기준점 (x, y)와 경계의 길이 d1, d2를 정한다. (d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N)
# 다음 칸은 경계선이다.
# (x, y), (x+1, y-1), ..., (x+d1, y-d1)
# (x, y), (x+1, y+1), ..., (x+d2, y+d2)
# (x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
# (x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)
# 경계선과 경계선의 안에 포함되어있는 곳은 5번 선거구이다.
# 5번 선거구에 포함되지 않은 구역 (r, c)의 선거구 번호는 다음 기준을 따른다.
# 1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
# 2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
# 3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
# 4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
# 아래는 크기가 7×7인 재현시를 다섯 개의 선거구로 나눈 방법의 예시이다.
#
# 구역 (r, c)의 인구는 A[r][c]이고, 선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값이다. 선거구를 나누는 방법 중에서, 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 구해보자.
#
# 입력
# 첫째 줄에 재현시의 크기 N이 주어진다.
#
# 둘째 줄부터 N개의 줄에 N개의 정수가 주어진다. r행 c열의 정수는 A[r][c]를 의미한다.
#
# 출력
# 첫째 줄에 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값을 출력한다.
#
# 제한
# 5 ≤ N ≤ 20
# 1 ≤ A[r][c] ≤ 100
import sys
n=int(input())
a=[[]]
for i in range(1, n+1):
    a.append([0]+list(map(int, input().split())))
def divide(y, x, d1, d2):
    answers=[0 for _ in range(6)]
    chk=[[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(d1+1):
        chk[y+i][x-i]=5
        chk[y+d2+i][x+d2-i]=5
    for i in range(d2+1):
        chk[y+i][x+i]=5
        chk[y+d1+i][x-d1+i]=5
    for i in range(y+1, y+d1+d2):
        chk_True=False
        for j in range(1, n+1):
            if chk[i][j]==5:
                chk_True=not chk_True
            if chk_True:
                chk[i][j]=5
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i<y+d1 and j<=x and chk[i][j]==0:
                answers[1]+=a[i][j]
            elif i<=y+d2 and x<j and chk[i][j]==0:
                answers[2]+=a[i][j]
            elif y+d1<=i and j<x-d1+d2 and chk[i][j]==0:
                answers[3]+=a[i][j]
            elif y+d2<i and x-d1+d2<=j and chk[i][j]==0:
                answers[4]+=a[i][j]
            elif chk[i][j]==5:
                answers[5]+=a[i][j]
    return max(answers[1:])-min(answers[1:])
answer=sys.maxsize
for i in range(n):
    for j in range(n):
        for d1 in range(n):
            for d2 in range(n):
                if 0<i<i+d1+d2<=n and 0<j-d1<j<j+d2<=n:
                    answer=min(divide(i, j, d1, d2), answer)
print(answer)