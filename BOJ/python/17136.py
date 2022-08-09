# 문제
# <그림 1>과 같이 정사각형 모양을 한 다섯 종류의 색종이가 있다. 색종이의 크기는 1×1, 2×2, 3×3, 4×4, 5×5로 총 다섯 종류가 있으며, 각 종류의 색종이는 5개씩 가지고 있다.
#
#
#
# <그림 1>
#
# 색종이를 크기가 10×10인 종이 위에 붙이려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 0 또는 1이 적혀 있다. 1이 적힌 칸은 모두 색종이로 덮여져야 한다. 색종이를 붙일 때는 종이의 경계 밖으로 나가서는 안되고, 겹쳐도 안 된다. 또, 칸의 경계와 일치하게 붙여야 한다. 0이 적힌 칸에는 색종이가 있으면 안 된다.
#
# 종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수를 구해보자.
#
# 입력
# 총 10개의 줄에 종이의 각 칸에 적힌 수가 주어진다.
#
# 출력
# 모든 1을 덮는데 필요한 색종이의 최소 개수를 출력한다. 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.
grid = [list(map(int, input().split())) for _ in range(10)]
cnts = [0 for _ in range(5)]
answer = 1e9
def chk(y, x, sz):
    for i in range(y, y+sz+1):
        for j in range(x, x+sz+1):
            if grid[i][j] == 0:
                return False
    return True
def find_min(y, x):
    global answer
    if y >= 10:
        answer = min(answer, sum(cnts))
        return
    if x >= 10:
        find_min(y+1, 0)
        return
    if grid[y][x] == 1:
        for sz in range(5):
            if cnts[sz] >= 5:
                continue
            if not (0 <= y + sz < 10 and 0 <= x + sz < 10):
                continue
            if chk(y, x, sz):
                for i in range(y, y+sz+1):
                    for j in range(x, x+sz+1):
                        grid[i][j] = 0
                cnts[sz] += 1
                find_min(y, x+sz+1)
                cnts[sz] -= 1
                for i in range(y, y+sz+1):
                    for j in range(x, x+sz+1):
                        grid[i][j] = 1
    else:
        find_min(y, x+1)
find_min(0, 0)
if answer == 1e9:
    answer = -1
print(answer)
