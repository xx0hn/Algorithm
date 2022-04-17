# 나이트
# 나이트는 다음과 같이 노란색 위치를 기준으로 검은색 8곳으로 움직임이 가능합니다. n * n 격자 위에서 격자를 벗어나지 않고 나이트가 시작점에서 도착점까지 가는 데 걸리는 최소 이동 횟수를 구하는 프로그램을 작성해보세요.



# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

# 두 번째 줄에는 나이트의 시작 위치 (r1, c1)와 끝 위치 (r2, c2)가 각각 공백을 사이에 두고 주어집니다. 이는 r1행 c1열 에서 r2행 c2열로 이동해야 함을 의미합니다. (1 ≤ r1, c1, r2, c2 ≤ n)

# 1 ≤ n ≤ 100
# 출력 형식
# 시작 위치에서 도착 위치까지 나이트가 도달하는 데 필요한 최소 이동 횟수를 출력합니다. 불가능하다면 -1을 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 5
# 3 3 3 2
# 출력:

# 3
# 예제2
# 입력:

# 3
# 3 3 1 1
# 출력:

# 4
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
from collections import deque
n=int(input())
points=list(map(int, input().split()))
sy, sx, ey, ex=points[0]-1, points[1]-1, points[2]-1, points[3]-1
dy=[-2, -2, -1, 1, 2, 2, 1, -1]
dx=[-1, 1, 2, 2, 1, -1, -2, -2]
visited=[[False for _ in range(n)] for _ in range(n)]
def bfs():
    q=deque()
    q.append((sy, sx, 0))
    visited[sy][sx]=True
    while q:
        y, x, cnt=q.popleft()
        if (y, x)==(ey, ex):
            print(cnt)
            quit()
        for i in range(8):
            ny, nx=y+dy[i], x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny, nx, cnt+1))
bfs()
print(-1)
