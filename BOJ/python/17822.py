# 문제
# 반지름이 1, 2, ..., N인 원판이 크기가 작아지는 순으로 바닥에 놓여있고, 원판의 중심은 모두 같다. 원판의 반지름이 i이면, 그 원판을 i번째 원판이라고 한다. 각각의 원판에는 M개의 정수가 적혀있고, i번째 원판에 적힌 j번째 수의 위치는 (i, j)로 표현한다. 수의 위치는 다음을 만족한다.
#
# (i, 1)은 (i, 2), (i, M)과 인접하다.
# (i, M)은 (i, M-1), (i, 1)과 인접하다.
# (i, j)는 (i, j-1), (i, j+1)과 인접하다. (2 ≤ j ≤ M-1)
# (1, j)는 (2, j)와 인접하다.
# (N, j)는 (N-1, j)와 인접하다.
# (i, j)는 (i-1, j), (i+1, j)와 인접하다. (2 ≤ i ≤ N-1)
# 아래 그림은 N = 3, M = 4인 경우이다.
#
# 원판의 회전은 독립적으로 이루어진다. 2번 원판을 회전했을 때, 나머지 원판은 회전하지 않는다. 원판을 회전시킬 때는 수의 위치를 기준으로 하며, 회전시킨 후의 수의 위치는 회전시키기 전과 일치해야 한다.
#
# 다음 그림은 원판을 회전시킨 예시이다.
#
# 원판을 아래와 같은 방법으로 총 T번 회전시키려고 한다. 원판의 회전 방법은 미리 정해져 있고, i번째 회전할때 사용하는 변수는 xi, di, ki이다.
#
# 번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
# 원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
# 그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
# 없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
# 원판을 T번 회전시킨 후 원판에 적힌 수의 합을 구해보자.
#
# 입력
# 첫째 줄에 N, M, T이 주어진다.
#
# 둘째 줄부터 N개의 줄에 원판에 적힌 수가 주어진다. i번째 줄의 j번째 수는 (i, j)에 적힌 수를 의미한다.
#
# 다음 T개의 줄에 xi, di, ki가 주어진다.
#
# 출력
# 원판을 T번 회전시킨 후 원판에 적힌 수의 합을 출력한다.
#
# 제한
# 2 ≤ N, M ≤ 50
# 1 ≤ T ≤ 50
# 1 ≤ 원판에 적힌 수 ≤ 1,000
# 2 ≤ xi ≤ N
# 0 ≤ di ≤ 1
# 1 ≤ ki < M
from collections import deque
n, m, t=map(int, input().split())
board=[deque(list(map(int, input().split()))) for _ in range(n)]
cycle=[]
for _ in range(t):
    x, d, k=map(int, input().split())
    cycle.append((x-1, d, k))
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def cycling(x, d, k):
    if d==0:
        d=1
    else:
        d=-1
    for _ in range(k):
        board[x].rotate(d)
def removing():
    idxs=set()
    for i in range(n):
        for j in range(m):
            tmp_idx=[]
            for d in range(4):
                ny, nx=i+dy[d], (j+dx[d])%m
                if 0<=ny<n and board[ny][nx]>0 and board[ny][nx]==board[i][j]:
                    tmp_idx.append((ny, nx))
            if tmp_idx:
                tmp_idx.append((i, j))
            for y, x in tmp_idx:
                idxs.add((y, x))
    if idxs:
        for y, x in idxs:
            board[y][x]=0
    elif not idxs:
        avg=0
        cnt=0
        for i in range(n):
            for j in range(m):
                if board[i][j]>0:
                    avg+=board[i][j]
                    cnt+=1
        if cnt>0 and avg>=0:
            avg/=cnt
            for i in range(n):
                for j in range(m):
                    if board[i][j]>0:
                        if board[i][j]>avg:
                            board[i][j]-=1
                        elif board[i][j]<avg:
                            board[i][j]+=1
for i in range(t):
    cnt=cycle[i][0]+1
    cycling(cycle[i][0], cycle[i][1], cycle[i][2])
    while cycle[i][0]+cnt<n:
        cycling(cycle[i][0]+cnt, cycle[i][1], cycle[i][2])
        cnt+=(cycle[i][0]+1)
    removing()
answer=0
for i in range(n):
    for j in range(m):
        answer+=board[i][j]
print(answer)
