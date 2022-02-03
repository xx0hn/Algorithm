# 문제
# 간단하지만 귀찮은 영상처리 과제가 주어졌다. 과제의 명세는 다음과 같다.
#
# 세로 길이가 $N$이고 가로 길이가 $M$인 화면은 총 $N$ × $M$개의 픽셀로 구성되어 있고 $(i, j)$에 있는 픽셀은 $R_{i,j}$ (Red), $G_{i,j}$ (Green), $B_{i,j}$ (Blue) 3가지 색상의 의미를 담고 있다. 각 색상은 0이상 255이하인 값으로 표현 가능하다.
#
# 모든 픽셀에서 세 가지 색상을 평균내어 경계값 $T$보다 크거나 같으면 픽셀의 값을 255로, 작으면 0으로 바꿔서 새로운 화면으로 저장한다.
#
# 새로 만들어진 화면에서 값이 255인 픽셀은 물체로 인식한다. 값이 255인 픽셀들이 상하좌우로 인접해있다면 이 픽셀들은 같은 물체로 인식된다.
#
# 화면에서 물체가 총 몇 개 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 화면의 세로 $N$, 가로 $M$ 값이 공백으로 구분되어 주어진다.
#
# 두 번째 줄부터 $N + 1$줄까지 $i$번째 가로를 구성하고 있는 픽셀의 $R_{i,j}$, $G_{i,j}$, $B_{i,j}$의 값이 공백으로 구분되어 총 $M$개 주어진다.
#
# 마지막 줄에는 경계값 $T$가 주어진다.
#
# 출력
# 화면에 있는 물체의 개수를 출력하라. 만약 물체가 없으면 0을 출력하면 된다.
#
# 제한
#  $1 \le N, M \le 1,000$ 
#  $0 \le R_{i,j}, G_{i,j}, B_{i,j} \le 255$, $R_{i,j}, G_{i,j}, B_{i,j}$ 값은 정수
#  $0 \le T \le 255$, $T$ 값은 정수
import sys
sys.setrecursionlimit(10**9)
def dfs(y, x):
    screen[y][x]=0
    dy=[0, 0, -1, 1]
    dx=[1, -1, 0, 0]
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if ny>=0 and nx>=0 and ny<n and nx<m and screen[ny][nx]>=t:
            dfs(ny, nx)

n, m=map(int, input().split())
screen=[]
for _ in range(n):
    tmp=list(map(int, input().split()))
    tmp_list=[]
    for i in range(m):
        tmp_list.append(sum(tmp[3*i:3*(i+1)])//3)
    screen.append(tmp_list)
t=int(input())
cnt=0
for i in range(n):
    for j in range(m):
        if screen[i][j]>=t:
            dfs(i, j)
            cnt+=1
print(cnt)
