# 문제
# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
#
#
#
# 입력
# 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
#
# 각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.
#
# 출력
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
import collections
t=int(input())
for _ in range(t):
    l=int(input())
    f_y, f_x=map(int, input().split())
    t_y, t_x=map(int, input().split())
    dy=[2, 2, -2, -2, 1, 1, -1, -1]
    dx=[-1, 1, 1, -1, 2, -2, 2, -2]
    visited=[[False]*l for _ in range(l)]
    visited[f_y][f_x]=True
    q=collections.deque()
    q.append((0, f_y, f_x))
    while q:
        cnt, y, x=q.popleft()
        if y==t_y and x==t_x:
            print(cnt)
            break
        for i in range(8):
            ny=y+dy[i]
            nx=x+dx[i]
            nxt_cnt=cnt+1
            if 0<=ny<l and 0<=nx<l and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((nxt_cnt, ny, nx))
