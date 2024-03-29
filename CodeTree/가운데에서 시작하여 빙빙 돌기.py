# 가운데에서 시작하여 빙빙 돌기
# n * n크기의 직사각형의 가운데에서 시작하여 오른쪽, 위, 왼쪽, 아래 순서로 더 이상 채울 곳이 없을 때까지 회전하며 숫자를 적어나가려고 합니다. 숫자는 1부터 시작한다고 했을 때, 다음과 같은 모양으로 숫자들을 쭉 채우는 코드를 작성해보세요.



# 입력 형식
# 첫 번째 줄에 크기를 나타내는 n이 주어집니다. 주어지는 n은 항상 홀수라고 가정해도 좋습니다.

# 1 ≤ n ≤ 100
# 출력 형식
# 숫자로 채워진 완성된 형태의 n * n 크기의 사각형을 출력합니다.
# (숫자끼리는 공백을 사이에 두고 출력합니다.)

# 입출력 예제
# 예제1
# 입력:

# 3
# 출력:

# 5 4 3
# 6 1 2
# 7 8 9
# 예제2
# 입력:

# 5
# 출력:

# 17 16 15 14 13
# 18 5 4 3 12
# 19 6 1 2 11
# 20 7 8 9 10
# 21 22 23 24 25
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
grid=[[0 for _ in range(n)] for _ in range(n)]
grid[n-1][n-1]=n**2
dy=[0, -1, 0, 1]
dx=[-1, 0, 1, 0]
y, x, d=n-1, n-1, 0
for i in range(n**2-1, 0, -1):
    ny=y+dy[d]
    nx=x+dx[d]
    if not (0<=ny<n and 0<=nx<n) or grid[ny][nx]!=0:
        d=(d+1)%4
        ny=y+dy[d]
        nx=x+dx[d]
    grid[ny][nx]=i
    y, x=ny, nx
for i in range(n):
    print(*grid[i])
