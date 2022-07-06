# 문제
# 스도쿠는 매우 간단한 숫자 퍼즐이다. 9×9 크기의 보드가 있을 때, 각 행과 각 열, 그리고 9개의 3×3 크기의 보드에 1부터 9까지의 숫자가 중복 없이 나타나도록 보드를 채우면 된다. 예를 들어 다음을 보자.
#
#
#
# 위 그림은 참 잘도 스도쿠 퍼즐을 푼 경우이다. 각 행에 1부터 9까지의 숫자가 중복 없이 나오고, 각 열에 1부터 9까지의 숫자가 중복 없이 나오고, 각 3×3짜리 사각형(9개이며, 위에서 색깔로 표시되었다)에 1부터 9까지의 숫자가 중복 없이 나오기 때문이다.
#
# 하다 만 스도쿠 퍼즐이 주어졌을 때, 마저 끝내는 프로그램을 작성하시오.
#
# 입력
# 9개의 줄에 9개의 숫자로 보드가 입력된다. 아직 숫자가 채워지지 않은 칸에는 0이 주어진다.
#
# 출력
# 9개의 줄에 9개의 숫자로 답을 출력한다. 답이 여러 개 있다면 그 중 사전식으로 앞서는 것을 출력한다. 즉, 81자리의 수가 제일 작은 경우를 출력한다.
#
# 제한
# 12095번 문제에 있는 소스로 풀 수 있는 입력만 주어진다.
# C++17: 180ms
# Java 15: 528ms
# PyPy3: 2064ms
grid = [list(str(input())) for _ in range(9)]
answer = []
zeros = []
for i in range(9):
    for j in range(9):
        if grid[i][j] == '0':
            zeros.append((i, j))
def chk_rc(r, c, num):
    for i in range(9):
        if grid[r][i] == num:
            return False
        if grid[i][c] == num:
            return False
    return True
def chk(r, c, num):
    nr, nc = (r//3) * 3, (c//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[nr+i][nc+j] == num:
                return False
    return True
def make_grid(cur):
    if cur == len(zeros):
        for i in range(9):
            print(''.join(grid[i]))
        quit()
    y, x = zeros[cur]
    for num in range(1, 10):
        if chk_rc(y, x, str(num)) and chk(y, x, str(num)):
            grid[y][x] = str(num)
            make_grid(cur+1)
            grid[y][x] = '0'
make_grid(0)
