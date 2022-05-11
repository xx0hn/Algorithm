# 문제
# 형택이는 1부터 9까지의 숫자와, 구멍이 있는 직사각형 보드에서 재밌는 게임을 한다.
#
# 일단 보드의 가장 왼쪽 위에 동전을 하나 올려놓는다. 그다음에 다음과 같이 동전을 움직인다.
#
# 동전이 있는 곳에 쓰여 있는 숫자 X를 본다.
# 위, 아래, 왼쪽, 오른쪽 방향 중에 한가지를 고른다.
# 동전을 위에서 고른 방향으로 X만큼 움직인다. 이때, 중간에 있는 구멍은 무시한다.
# 만약 동전이 구멍에 빠지거나, 보드의 바깥으로 나간다면 게임은 종료된다. 형택이는 이 재밌는 게임을 되도록이면 오래 하고 싶다.
#
# 보드의 상태가 주어졌을 때, 형택이가 최대 몇 번 동전을 움직일 수 있는지 구하는 프로그램을 작성하시오.
#
# 입력
# 줄에 보드의 세로 크기 N과 가로 크기 M이 주어진다. 이 값은 모두 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 보드의 상태가 주어진다. 쓰여 있는 숫자는 1부터 9까지의 자연수 또는 H이다. 가장 왼쪽 위칸은 H가 아니다. H는 구멍이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 형택이가 동전을 무한번 움직일 수 있다면 -1을 출력한다.
n, m=map(int, input().split())
board=[str(input()) for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
dp=[[0 for _ in range(m)] for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
answer=-1
def get_answer(y, x, cnt):
    global answer
    answer=max(answer, cnt)
    for i in range(4):
        ny, nx=y+int(board[y][x])*dy[i], x+int(board[y][x])*dx[i]
        if 0<=ny<n and 0<=nx<m and board[ny][nx]!='H' and cnt+1>dp[ny][nx]:
            if visited[ny][nx]:
                answer=-1
                print(answer)
                quit()
            else:
                dp[ny][nx]=cnt+1
                visited[ny][nx]=True
                get_answer(ny, nx, cnt+1)
                visited[ny][nx]=False
get_answer(0, 0, 0)
print(answer+1)
