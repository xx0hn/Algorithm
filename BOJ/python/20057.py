# 문제
# 마법사 상어가 토네이도를 배웠고, 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다. 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.
#
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다. 다음은 N = 7인 경우 토네이도의 이동이다.
#
#
#
# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
#
#
#
# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다. α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다. 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.
#
# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.
#
# 입력
# 첫째 줄에 격자의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
#
# 출력
# 격자의 밖으로 나간 모래의 양을 출력한다.
#
# 제한
# 3 ≤ N ≤ 499
# N은 홀수
# 0 ≤ A[r][c] ≤ 1,000
# 가운데 칸에 있는 모래의 양은 0
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]
answer=0
dy, dx=[0, 1, 0, -1], [-1, 0, 1, 0]
def spread(dust, ny, nx, d):
    a=0
    if 0<=ny+2*dy[(d+1)%4]<n and 0<=nx+2*dx[(d+1)%4]<n:
        grid[ny+2*dy[(d+1)%4]][nx+2*dx[(d+1)%4]]+=int(dust*0.02)
    if 0<=ny+2*dy[(d+3)%4]<n and 0<=nx+2*dx[(d+3)%4]<n:
        grid[ny+2*dy[(d+3)%4]][nx+2*dx[(d+3)%4]]+=int(dust*0.02)
    a+=2*int(dust*0.02)
    if 0<=ny+dy[(d+1)%4]<n and 0<=nx+dx[(d+1)%4]<n:
        grid[ny+dy[(d+1)%4]][nx+dx[(d+1)%4]]+=int(dust*0.07)
    if 0<=ny+dy[(d+3)%4]<n and 0<=nx+dx[(d+3)%4]<n:
        grid[ny+dy[(d+3)%4]][nx+dx[(d+3)%4]]+=int(dust*0.07)
    a+=2*int(dust*0.07)
    if 0<=ny+2*dy[d]<n and 0<=nx+2*dx[d]<n:
        grid[ny+2*dy[d]][nx+2*dx[d]]+=int(dust*0.05)
    a+=int(dust*0.05)
    if d%2==0:
        if 0<=ny+dy[(d+1)%4]<n and 0<=nx+dx[d]<n:
            grid[ny+dy[(d+1)%4]][nx+dx[d]]+=int(dust*0.1)
        if 0<=ny+dy[(d+3)%4]<n and 0<=nx+dx[d]<n:
            grid[ny+dy[(d+3)%4]][nx+dx[d]]+=int(dust*0.1)
        a+=2*int(dust*0.1)
        if 0<=ny+dy[(d+1)%4]<n and 0<=nx+dx[(d+2)%4]<n:
            grid[ny+dy[(d+1)%4]][nx+dx[(d+2)%4]]+=int(dust*0.01)
        if 0<=ny+dy[(d+3)%4]<n and 0<=nx+dx[(d+2)%4]<n:
            grid[ny+dy[(d+3)%4]][nx+dx[(d+2)%4]]+=int(dust*0.01)
        a+=2*int(dust*0.01)
    if d%2==1:
        if 0<=ny+dy[d]<n and 0<=nx+dx[(d+1)%4]<n:
            grid[ny+dy[d]][nx+dx[(d+1)%4]]+=int(dust*0.1)
        if 0<=ny+dy[d]<n and 0<=nx+dx[(d+3)%4]<n:
            grid[ny+dy[d]][nx+dx[(d+3)%4]]+=int(dust*0.1)
        a+=2*int(dust*0.1)
        if 0<=ny+dy[(d+2)%4]<n and 0<=nx+dx[(d+1)%4]<n:
            grid[ny+dy[(d+2)%4]][nx+dx[(d+1)%4]]+=int(dust*0.01)
        if 0<=ny+dy[(d+2)%4]<n and 0<=nx+dx[(d+3)%4]<n:
            grid[ny+dy[(d+2)%4]][nx+dx[(d+3)%4]]+=int(dust*0.01)
        a+=2*int(dust*0.01)
    if 0<=ny+dy[d]<n and 0<=nx+dx[d]<n:
        grid[ny+dy[d]][nx+dx[d]]+=(dust-a)
    grid[ny][nx]=0
def wind(y, x):
    cnt, idx=0, 1
    for i in range(2*n-1):
        for j in range(1, idx+1):
            ny, nx=y+dy[i%4], x+dx[i%4]
            if 0<=ny<n and 0<=nx<n:
                spread(grid[ny][nx], ny, nx, i%4)
                y, x=ny, nx
        cnt+=1
        if cnt==2:
            cnt=0
            idx+=1
for i in range(n):
    for j in range(n):
        answer+=grid[i][j]
wind(n//2, n//2)
for i in range(n):
    for j in range(n):
        answer-=grid[i][j]
print(answer)
