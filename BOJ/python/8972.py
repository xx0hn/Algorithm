# 문제
# 요즘 종수는 아두이노를 이용해 "Robots"이라는 게임을 만들었다. 종수는 아두이노 한대를 조정하며, 미친 아두이노를 피해다녀야 한다. 미친 아두이노는 종수의 아두이노를 향해 점점 다가온다. 하지만, 미친 아두이노의 움직임은 예측할 수 있다.
#
# 게임은 R×C크기의 보드 위에서 이루어지며, 아래와 같은 5가지 과정이 반복된다.
#
# 먼저, 종수가 아두이노를 8가지 방향(수직,수평,대각선)으로 이동시키거나, 그 위치에 그대로 놔둔다.
# 종수의 아두이노가 미친 아두이노가 있는 칸으로 이동한 경우에는 게임이 끝나게 되며, 종수는 게임을 지게 된다.
# 미친 아두이노는 8가지 방향 중에서 종수의 아두이노와 가장 가까워 지는 방향으로 한 칸 이동한다. 즉, 종수의 위치를 (r1,s1), 미친 아두이노의 위치를 (r2, s2)라고 했을 때, |r1-r2| + |s1-s2|가 가장 작아지는 방향으로 이동한다.
# 미친 아두이노가 종수의 아두이노가 있는 칸으로 이동한 경우에는 게임이 끝나게 되고, 종수는 게임을 지게 된다.
# 2개 또는 그 이상의 미친 아두이노가 같은 칸에 있는 경우에는 큰 폭발이 일어나고, 그 칸에 있는 아두이노는 모두 파괴된다.
# 종수의 시작 위치, 미친 아두이노의 위치, 종수가 움직이려고 하는 방향이 주어진다. 입력으로 주어진 방향대로 종수가 움직였을 때, 보드의 상태를 구하는 프로그램을 작성하시오. 중간에 게임에서 지게된 경우에는 몇 번째 움직임에서 죽는지를 구한다.
#
# 입력
# 첫째 줄에 보드의 크기 R과 C가 주어진다. (1 ≤ R, C ≤ 100)
#
# 다음 R개 줄에는 C개의 문자가 주어지며, 보드의 상태이다. '.'는 빈 칸, 'R'은 미친 아두이노, 'I'는 종수의 위치를 나타낸다.
#
# 마지막 줄에는 길이가 100을 넘지않는 문자열이 주어지며, 종수가 움직이려고 하는 방향이다. 5는 그 자리에 그대로 있는 것을 나타내고, 나머지는 아래와 같은 방향을 나타낸다.
#
#
#
# 보드를 벗어나는 입력은 주어지지 않는다.
#
# 출력
# 중간에 게임이 끝나는 경우에는 "kraj X"를 출력한다. X는 종수가 게임이 끝나기 전 까지 이동한 횟수이다. 그 외의 경우에는 보드의 상태를 입력과 같은 형식으로 출력한다.
from collections import defaultdict
r, c=map(int, input().split())
grid=[list(str(input())) for _ in range(r)]
user=[]
mad=[]
for i in range(r):
    for j in range(c):
        if grid[i][j]=='I':
            user=(i, j)
        if grid[i][j]=='R':
            mad.append((i, j))
coms=str(input())
dy, dx=[0, 1, 1, 1, 0, 0, 0, -1, -1, -1], [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
def move_I(num):
    global user
    user=(user[0]+dy[int(coms[num])], user[1]+dx[int(coms[num])])
    if 0<=user[0]<r and 0<=user[1]<c:
        if (user[0], user[1]) in set(mad):
            print("kraj {0}".format(num+1))
            quit()
def move_R(num):
    global mad
    counting=defaultdict(int)
    for i in range(len(mad)):
        y, x=mad[i][0], mad[i][1]
        tmp=1e9
        d=-1
        for j in range(1, 10):
            ny, nx=y+dy[j], x+dx[j]
            if 0<=ny<r and 0<=nx<c:
                dist=abs(ny-user[0])+abs(nx-user[1])
                if dist<tmp:
                    tmp=dist
                    d=j
        mad[i]=(mad[i][0]+dy[d], mad[i][1]+dx[d])
        counting[mad[i]]+=1
        if mad[i]==user:
            print("kraj {0}".format(num+1))
            quit()
    new_mad=[]
    for i in range(len(mad)):
        if counting[mad[i]]>1:
            continue
        else:
            new_mad.append(mad[i])
    mad=new_mad[:]
for i in range(len(coms)):
    move_I(i)
    move_R(i)
answer=[['.' for _ in range(c)] for _ in range(r)]
answer[user[0]][user[1]]='I'
for y, x in mad:
    if y==-1 and x==-1:
        continue
    answer[y][x]='R'
for i in range(r):
    print(''.join(answer[i]))
