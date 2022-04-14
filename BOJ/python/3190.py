# 문제
#  'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
#
# 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
#
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
#
# 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
# 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
#
# 입력
# 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)
#
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.
#
# 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)
#
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.
#
# 출력
# 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.
import collections
import sys

n=int(input())
k=int(input())
grid=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(k):
    r, c=map(int, input().split())
    grid[r-1][c-1]=2
l=int(input())
command=[list(map(str, input().split())) for _ in range(l)]
for i in range(l-1, 0, -1):
    command[i][0]=int(command[i][0])-int(command[i-1][0])
command.append([sys.maxsize, ''])
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def move(y, x, d):
    result=0
    tail=collections.deque()
    tail.append((y, x))
    for com in command:
        for i in range(1, int(com[0])+1):
            ny, nx=tail[-1][0]+dy[d], tail[-1][1]+dx[d]
            if 0<=ny<n and 0<=nx<n:
                if (ny, nx) in tail:
                    return result+1
                tail.append((ny, nx))
                if grid[ny][nx]!=2:
                    tail.popleft()
                else:
                    grid[ny][nx]=0
                result+=1
            else:
                return result+1
        if com[1]=='L':
            d=(d+3)%4
        elif com[1]=='D':
            d=(d+1)%4
    return result+1
answer=move(0, 0, 0)
print(answer)
