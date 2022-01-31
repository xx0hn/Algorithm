# 문제
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
#
#
#
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
#
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
#
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
#
# 입력의 마지막 줄에는 0이 두 개 주어진다.
#
# 출력
# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
import sys
sys.setrecursionlimit(10**9)
while True:
    w, h=map(int, input().split())
    if w==0 and h==0:
        break
    island=[]
    visited=[[False]*w for _ in range(h)]
    dh=[1, -1, 0, 0, 1, 1, -1, -1]
    dw=[0, 0, 1, -1, 1, -1, 1, -1]
    cnt=0
    def dfs(w_tmp, h_tmp):
        visited[h_tmp][w_tmp]=True
        for i in range(8):
            next_w=w_tmp+dw[i]
            next_h=h_tmp+dh[i]
            if next_w>=0 and next_h>=0 and next_w<w and next_h<h:
                if visited[next_h][next_w]==False and island[next_h][next_w]==1:
                    dfs(next_w, next_h)
    for i in range(h):
        island.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if island[i][j]==1 and visited[i][j]==False:
                dfs(j, i)
                cnt+=1
    print(cnt)
