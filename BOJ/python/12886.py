# 문제
# 오늘 강호는 돌을 이용해 재미있는 게임을 하려고 한다. 먼저, 돌은 세 개의 그룹으로 나누어져 있으며 각각의 그룹에는 돌이 A, B, C개가 있다. 강호는 모든 그룹에 있는 돌의 개수를 같게 만들려고 한다.
#
# 강호는 돌을 단계별로 움직이며, 각 단계는 다음과 같이 이루어져 있다.
#
# 크기가 같지 않은 두 그룹을 고른다. 그 다음, 돌의 개수가 작은 쪽을 X, 큰 쪽을 Y라고 정한다. 그 다음, X에 있는 돌의 개수를 X+X개로, Y에 있는 돌의 개수를 Y-X개로 만든다.
#
# A, B, C가 주어졌을 때, 강호가 돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 A, B, C가 주어진다. (1 ≤ A, B, C ≤ 500)
#
# 출력
# 돌을 같은 개수로 만들 수 있으면 1을, 아니면 0을 출력한다.
from collections import deque
a, b, c=map(int, input().split())
s=a+b+c
visited=[[False for _ in range(s)] for _ in range(s)]
def bfs():
    q=deque()
    q.append((a, b))
    visited[a][b]=True
    while q:
        i, j=q.popleft()
        k=s-j-i
        if i==j==k:
            return 1
        for x, y in (i, j), (j, k), (k, i):
            if x<y:
                x+=x
                y-=x
            elif x>y:
                x-=y
                y+=y
            else:
                continue
            z=s-x-y
            nx=min(x, y, z)
            ny=max(x, y, z)
            if 0<=nx and 0<=ny and 0<=s-nx-ny:
                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny]=True
    return 0
answer=0
if not s%3:
    answer=bfs()
print(answer)
