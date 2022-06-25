# 문제
# 갤러리의 지도는 M*N의 정사각형 격자로 표현될 수 있다. 어떤 정사각형들은 벽으로 구성되어 있고, 다른 정사각형들은 빈 공간으로 구성되어 있다. 벽을 회색, 빈 공간을 흰색으로 표현하면 다음 그림과 같다.
# 
# 
# 
# 갤러리에 그림을 걸려고 한다. 그림의 길이는 정사각형의 변의 길이의 두 배이다. 반드시 빈 공간과 인접해 있는 벽에만 그림을 걸 수 있으며, 그림들은 서로 겹칠 수 없다. 갤러리의 맵이 주어졌을 때, 최대로 걸 수 있는 그림의 개수를 출력하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 갤러리의 세로 길이 M과 가로 길이 N이 주어진다. (1 ≤ M, N ≤ 1,000) 다음 M개의 줄에는 각각 N개의 문자가 주어진다. 문자는 'X' 또는 '.'이며 'X'는 벽을, '.'는 빈 공간을 나타낸다.
# 
# 입력되는 모든 데이터에서 적어도 첫 줄과 마지막 줄, 첫 열과 마지막 열은 모두 벽이다.
# 
# 출력
# 최대 그림 개수를 출력한다.
m, n = map(int, input().split())
grid = [str(input()) for _ in range(m)]
using = [[[False for _ in range(n)] for _ in range(m)] for _ in range(4)]
answer = 0
def find_max():
    global answer
    for i in range(1, m-1):
        for j in range(1, n-1):
            if grid[i][j] == '.':
                if grid[i][j+1] == '.':
                    if grid[i+1][j] == 'X' and grid[i+1][j+1] == 'X' and not using[0][i][j]:
                        using[0][i][j] = True
                        using[0][i][j+1] = True
                        answer += 1
                    if grid[i-1][j] == 'X' and grid[i-1][j+1] == 'X' and not using[1][i][j]:
                        using[1][i][j] = True
                        using[1][i][j+1] = True
                        answer += 1
                if grid[i+1][j] == '.':
                    if grid[i][j+1] == 'X' and grid[i+1][j+1] == 'X' and not using[2][i][j]:
                        using[2][i][j] = True
                        using[2][i+1][j] = True
                        answer += 1
                    if grid[i][j-1] == 'X' and grid[i+1][j-1] == 'X' and not using[3][i][j]:
                        using[3][i][j] = True
                        using[3][i+1][j] = True
                        answer += 1
find_max()
print(answer)
