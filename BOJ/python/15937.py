# 문제
# 2차원 좌표 평면 위에 두 개의 박스(직사각형) P, Q가 놓여 있다. 각 박스의 변은 x축이나 y축에 평행하다. 박스를 연구하는 학수는 이 두 박스의 교차 상태를 파악하여 내부가 겹쳐 있는지 (FACE), 그렇지 않고 선분에서 만나는 지(LINE), 그렇지 않고 한 점에서 만나는지(POINT), 아예 만나지 않는지 (NULL) 구별하려고 한다.
#
# 다음 그림은 두 박스의 여러 가지 교차 상태의 예를 보여준다.
#
# (a) POINT	(b) LINE	(c) FACE	(d) FACE	(e) NULL
#
# FACE인 경우에는 (d)처럼 어느 한 박스가 다른 박스에 포함될 수도 있다는 점에 유의해야 한다.
#
# 두 박스의 정보가 주어졌을 때, 두 박스의 교차 상태를 출력하는 프로그램을 작성하시오.
#
# 입력
# 표준 입력으로 두 박스의 정보가 한 줄에 하나씩 주어진다. 각 박스의 정보는 왼쪽 아래 꼭짓점 좌표 (x1, y1)과 오른쪽 위 꼭짓점 좌표 (x2, y2)로 구성되는데 이들 좌푯값 x1, y1, x2, y2 (x1 < x2, y1 < y2)가 공백을 사이에 두고 주어진다.
#
# 출력
# 표준 출력으로 두 박스의 교차 상태를 POINT, LINE, FACE, NULL 중의 하나로 출력한다. 두 박스의 교차 상태는 모두 대문자로 출력한다.
#
# 제한
# 모든 서브태스크에서 x좌표와 y좌표는 모두 -109 이상 109 이하인 정수이다.
#
# 서브태스크 1 (33점)
# POINT나 LINE인 경우만 있다.
#
# 서브태스크 2 (30점)
# 모든 좌푯값이 0 이상 1,000 이하이다.
#
# 서브태스크 3 (37점)
# 원래의 제약조건 이외에 아무 제약조건이 없다.


# ax, ay, bx, by=map(int, input().split())
# cx, cy, dx, dy=map(int, input().split())
# mx_num=max(ax, ay, bx, by, cx, cy, dx, dy)
# graph=[[0]*(mx_num+1) for _ in range(mx_num+1)]
# for x in range(ax, bx+1):
#     graph[x][ay:by+1]=[1]*(by-ay+1)
# for x in range(cx, dx+1):
#     graph[x][cy:dy+1]=[1]*(dy-cy+1)
# dx=[0, 0, -1, 1]
# dy=[1, -1, 0, 0]
# visited=[[False]*(mx_num+1) for _ in range(mx_num+1)]
# def get_width(x, y, result):
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<=mx_num and 0<=ny<=mx_num and graph[nx][ny]==1 and not visited[nx][ny]:
#             visited[nx][ny]=True
#             result=get_width(nx, ny, result+1)
#     return result
# cur=0
# for i in range(mx_num+1):
#     for j in range(mx_num+1):
#         if graph[i][j]==1 and not visited[i][j]:
#             cur+=get_width(i, j, 0)
# origin=(ax-bx+1)*(ay-by+1)+(cx-dx+1)*(dy1-cy+1)
# if origin-cur==1:
#     print('POINT')
# elif origin-cur>1:
#     if bx==cx or by==cy:
#         print('LINE')
#     else:
#         print('FACE')
# elif origin-cur==0:
#     print('NULL')

ax, ay, bx, by=map(int, input().split())
cx, cy, dx, dy=map(int, input().split())
def point():
    if (ax,ay)==(dx,dy) or (bx,by)==(cx,cy) or (bx,ay)==(cx,dy) or (ax,by)==(dx,cy):
        return True
    else:
        return False
def line():
    if (((bx, by) == (cx, dy) and by > cy) or (((bx, ay) == (cx, cy) and dy > ay)) or ((dx, cy) == (ax, ay) and by > cy) or ((dx, dy) == (ax, by) and dy > ay) or ((bx, by) == (cx, dy) and (bx, ay) == (cx, cy)) or ((ax, ay) == (dx, cy) and (dx, dy) == (ax, by)) or ((cx, cy) == (ax, by) and (bx, by) == (dx, cy)) or ((ax, ay) == (cx, dy) and (dx, dy) == (bx, ay)) or (ax == dx and (ay < cy < by or ay < dy < by)) or (bx == cx and (ay < cy < by or ay < dy < by)) or (by == cy and (ax < cx < bx or ax < dx < bx)) or (ay == dy and (ax < cx < bx or ax < dx < bx)) or (ax == dx and (cy < ay < dy or cy < by < dy)) or (bx == cx and (cy < ay < dy or cy < by < dy)) or (by == cy and (cx < ax < dx or cx < bx < dx)) or (ay == dy and (cx < ax < dx or cx < bx < dx))):
        return True
    else:
        return False
def null():
    if bx<cx or dx<ax or by<cy or dy<ay:
        return True
    elif bx-ax<dx-cx and by-ay<dy-cy and (cx<ax<dx and cx<bx<dx) and (cy<ay<dy and cy<by<dy):
        return True
    elif bx-ax>dx-cx and by-ay>dy-cy and (ax<cx<bx and ax<dx<bx) and (ay<cy<by and ay<dy<by):
        return True
    else:
        return False
if line():
    print('LINE')
elif point():
    print('POINT')
elif null():
    print('NULL')
else:
    print('FACE')
