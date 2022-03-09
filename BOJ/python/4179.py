# 문제
# 지훈이는 미로에서 일을 한다. 지훈이를 미로에서 탈출하도록 도와주자!
#
# 미로에서의 지훈이의 위치와 불이 붙은 위치를 감안해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부, 그리고 얼마나 빨리 탈출할 수 있는지를 결정해야한다.
#
# 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다)  이동한다.
#
# 불은 각 지점에서 네 방향으로 확산된다.
#
# 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
#
# 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.
#
# 입력
# 입력의 첫째 줄에는 공백으로 구분된 두 정수 R과 C가 주어진다. 단, 1 ≤ R, C ≤ 1000 이다. R은 미로 행의 개수, C는 열의 개수이다.
#
# 다음 입력으로 R줄동안 각각의 미로 행이 주어진다.
#
#  각각의 문자들은 다음을 뜻한다.
#
# #: 벽
# .: 지나갈 수 있는 공간
# J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# J는 입력에서 하나만 주어진다.
#
# 출력
# 지훈이가 불이 도달하기 전에 미로를 탈출 할 수 없는 경우 IMPOSSIBLE 을 출력한다.
#
# 지훈이가 미로를 탈출할 수 있는 경우에는 가장 빠른 탈출시간을 출력한다.
from collections import deque
import sys
input=sys.stdin.readline
r, c=map(int, input().split())
maze=[]
jq=deque()
fq=deque()
for i in range(r):
    maze.append(list(str(input())))
    for j in range(len(maze[-1])):
        if maze[i][j]=='J':
            jq.append((i, j))
            maze[i][j]='.'
        if maze[i][j]=='F':
            fq.append((i, j))
dy=[0, 0, -1, 1]
dx=[1, -1, 0, 0]
J=[[False]*c for _ in range(r)]
F=[[False]*c for _ in range(r)]
J[jq[0][0]][jq[0][1]]=0
for i in range(len(fq)):
    F[fq[i][0]][fq[i][1]]=0
def bfs():
    while fq:
        y, x=fq.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<r and 0<=nx<c and not F[ny][nx] and maze[ny][nx]!='#':
                F[ny][nx]=F[y][x]+1
                fq.append((ny, nx))
    while jq:
        y, x=jq.popleft()
        if y==0 or y==r-1 or x==0 or x==c-1:
            print(J[y][x]+1)
            quit()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<r and 0<=nx<c and not J[ny][nx] and maze[ny][nx]!='#' and (F[ny][nx]-1>J[y][x] or not F[ny][nx]):
                J[ny][nx]=J[y][x]+1
                jq.append((ny, nx))
bfs()
print('IMPOSSIBLE')
