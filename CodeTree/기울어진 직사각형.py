# 기울어진 직사각형
# 1~100 사이의 숫자로만 이루어져 있는 n * n 크기의 격자 정보가 주어집니다.



# 이때, 이 격자 내에 있는 기울어진 직사각형들을 살펴보려고 합니다.

# 기울어진 직사각형이란, 격자내에 있는 한 지점으로부터 체스의 비숍처럼 대각선으로 움직이며 반시계 순회를 했을 때 지나왔던 지점들의 집합을 일컫습니다. 이 때 반드시 아래에서 시작해서 1, 2, 3, 4번 방향순으로 순회해야하며 각 방향으로 최소 1번은 움직여야 합니다. 또한, 이동하는 도중 격자 밖으로 넘어가서는 안됩니다.



# 예를 들어 위의 규칙에 따라 다음과 같은 기울어진 직사각형을 2개 만들어 볼 수 있습니다.





# 가능한 기울어진 직사각형들 중 해당 직사각형을 이루는 지점에 적힌 숫자들의 합이 최대가 되도록 하는 프로그램을 작성해보세요.

# 위의 예에서는 다음과 같이 기울어진 직사각형을 잡게 되었을 때 합이 21이 되어 최대가 됩니다.



# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

# 두 번째 줄부터는 n개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며, 이 정보는 1에서 100사이의 숫자로 각각 공백을 사이에 두고 주어집니다.

# 3 ≤ n ≤ 20
# 출력 형식
# 가능한 기울어진 직사각형들 중 최대의 합을 출력해주세요.

# 입출력 예제
# 예제1
# 입력:

# 5
# 1 2 2 2 2
# 1 3 4 4 4
# 1 2 3 3 3
# 1 2 3 3 3
# 1 2 3 3 3
# 출력:

# 21
# 예제2
# 입력:

# 3
# 1 2 3
# 4 5 6
# 7 8 8
# 출력:

# 20
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]
dy=[-1, -1, 1, 1]
dx=[1, -1, -1, 1]
def move(y, x, h, w):
    tmp=[h, w, h, w]
    result=0
    for i in range(4):
        for _ in range(tmp[i]):
            y=y+dy[i]
            x=x+dx[i]
            if not(0<=y<n and 0<=x<n):
                return 0
            result += grid[y][x]
    return result
answers=[]
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                answers.append(move(i, j, k, l))
print(max(answers))
