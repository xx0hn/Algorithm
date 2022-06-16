# 문제
# 세로 N, 가로 M 크기의 상자가 있다. 이 상자 안에는 몇 개의 거울이 들어 있다. 상자를 위에서 봤을 때, 거울은 한 칸 안에 대각선 모양으로 들어있다고 한다. 또, 상자의 테두리를 따라서 칸마다 구멍이 뚫려 있다. 편의상 구멍은 왼쪽 위에 뚫려있는 것부터 시계 반대 방향으로 1, 2, …, 2N+2M 의 번호가 붙어 있다. 예를 들어 다음과 같은 경우를 보자.
#
#
#
# 이제 이 상자에 뚫려있는 구멍으로 빛을 쏜다고 생각해보자. 1번 구멍으로 쏠 경우에는 (1, 2)의 위치에 있는 거울에 반사되어 9번 구멍으로 빛이 가게 된다. 또, 2번 구멍으로 빛을 쏠 경우에는 (2, 2)의 위치에 있는 거울과 (1, 2)에 있는 거울에 차례로 반사되어 7번 구멍으로 빛이 나가게 된다.
#
# 이와 같이 상자의 모양이 주어졌을 때, 각 구멍으로 쏜 빛이 나가게 되는 구멍을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N, M (1 ≤ N, M ≤ 1,000)이 주어진다. 다음 N개의 줄에는 M개의 수로 상자의 모양이 주어진다. 거울이 있는 위치는 1로, 거울이 없는 위치는 0으로 주어진다. 거울은 / 모양으로만 놓일 수 있다고 하자.
#
# 출력
# 첫째 줄부터 차례로 1번 구멍으로 쏜 빛이 나가는 구멍의 번호, 2번 구멍으로 쏜 빛이 나가는 구멍의 번호, …, 2N+2M번 구멍으로 쏜 빛이 나가는 구멍의 번호를 출력한다.
from collections import deque
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
dy, dx=[-1, 0, 1, 0], [0, 1, 0, -1]
answer=[]
def get_result(y, x):
    if y==-1:
        return 2*n+2*m-x
    elif x==-1:
        return y+1
    elif y==n:
        return n+x+1
    else:
        return 2*n+m-y
def find_dir(d):
    if d==0:
        return 1
    elif d==1:
        return 0
    elif d==2:
        return 3
    else:
        return 2
def move(y, x, d):
    while 0<=y<n and 0<=x<m:
        if grid[y][x]==1:
            d=find_dir(d)
        y+=dy[d]
        x+=dx[d]
    answer.append(str(get_result(y, x)))
def move1(y, x, d):
    if grid[y][x]==1:
        d=find_dir(d)
    q=deque()
    q.append((y, x, d))
    while q:
        sy, sx, sd=q.popleft()
        ny, nx=sy+dy[sd], sx+dx[sd]
        if 0<=ny<n and 0<=nx<m:
            if grid[ny][nx]==1:
                sd=find_dir(sd)
            q.append((ny, nx, sd))
        else:
            answer.append(str(get_result(ny, nx)))
for i in range(n):
    move1(i, 0, 1)
for i in range(m):
    move1(n-1, i, 0)
for i in range(n-1, -1, -1):
    move1(i, m-1, 3)
for i in range(m-1, -1, -1):
    move1(0, i, 2)
print(*answer)
