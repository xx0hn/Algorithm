# 문제
# 어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.
#
# 입력
# 첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
#
# 출력
# 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
# import sys
# sys.setrecursionlimit(10**9)
# def dfs(y, x, cnt):
#     paper[y][x]=0
#     for i in range(4):
#         ny=y+dy[i]
#         nx=x+dx[i]
#         if ny>=0 and nx>=0 and ny<n and nx<m:
#             if paper[ny][nx]==1:
#                 cnt=dfs(ny, nx, cnt+1)
#     return cnt
# n, m=map(int, input().split())
# paper=[]
# for _ in range(n):
#     paper.append(list(map(int, input().split())))
# dy=[0, 0, -1, 1]
# dx=[1, -1, 0, 0]
# answer=0
# cnt=0
# for i in range(n):
#     for j in range(m):
#         if paper[i][j]==1:
#             answer=max(answer, dfs(i, j, 1))
#             cnt+=1
# print(cnt)
# print(answer)
from collections import deque
def bfs(y, x):
    paper[y][x]=0
    q=deque()
    q.append((y,x))
    cnt=1
    while q:
        y, x=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny>=0 and nx>=0 and ny<n and nx<m and paper[ny][nx]==1:
                q.append((ny, nx))
                paper[ny][nx]=0
                cnt+=1
    return cnt
n, m=map(int, input().split())
paper=[]
for _ in range(n):
    paper.append(list(map(int, input().split())))
dy=[0, 0, -1, 1]
dx=[1, -1, 0, 0]
answer=0
cnt=0
for i in range(n):
    for j in range(m):
        if paper[i][j]==1:
            answer=max(answer, bfs(i, j))
            cnt+=1
print(cnt)
print(answer)
