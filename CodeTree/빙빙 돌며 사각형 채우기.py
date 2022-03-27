# 빙빙 돌며 사각형 채우기
# n * m크기의 직사각형에 대문자 알파벳을 A부터 Z까지 순서대로 증가시키며 달팽이 모양으로 채우는 코드를 작성해보세요.

# 달팽이 모양이란 왼쪽 위 모서리에서 시작해서, 오른쪽, 아래쪽, 왼쪽, 위쪽 순서로 더 이상 채울 곳이 없을 때까지 회전하는 모양을 의미합니다.

# Z 이후에는 다시 A부터 채우기 시작합니다.

# n : 행(row), m : 열(column)을 의미합니다.



# 입력 형식
# n과 m이 공백을 사이에 두고 주어집니다.

# 1 ≤ n, m ≤ 100
# 출력 형식
# 알파벳으로 채워진 완성된 형태의 n * m 크기의 사각형을 출력합니다.

# (알파벳끼리는 공백을 사이에 두고 출력합니다.)

# 입출력 예제
# 예제1
# 입력:

# 4 4
# 출력:

# A B C D 
# L M N E 
# K P O F 
# J I H G
# 예제2
# 입력:

# 4 2
# 출력:

# A B 
# H C 
# G D 
# F E
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m=map(int, input().split())
grid=[['' for _ in range(m)] for _ in range(n)]
dy=[0, 1, 0, -1]
dx=[1, 0, -1, 0]
grid[0][0]='A'
y, x, d=0, 0, 0
for i in range(2, n*m+1):
    ny, nx=y+dy[d], x+dx[d]
    if not (0<=ny<n and 0<=nx<m) or grid[ny][nx]!='':
        d=(d+1)%4
        ny=y+dy[d]
        nx=x+dx[d]
    if grid[y][x]=='Z':
        grid[ny][nx]='A'
    else:
        grid[ny][nx]=chr(ord(grid[y][x])+1)
    y, x=ny, nx
for i in range(n):
    print(*grid[i])
