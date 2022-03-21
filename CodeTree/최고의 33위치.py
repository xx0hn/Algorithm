# 최고의 33위치
# N * N 크기의 격자 정보가 주어집니다. 이때 해당 위치에 동전이 있다면 1, 없다면 0이 주어집니다. N * N 격자를 벗어나지 않도록 3 * 3 크기의 격자를 적절하게 잘 잡아서 해당 범위 안에 들어있는 동전의 개수를 최대로 하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 N이 주어집니다.

# 두 번째 줄부터는 N개의 줄에 걸쳐 격자에 대한 정보가 주어집니다. 각 줄에는 각각의 행에 대한 정보가 주어지며, 이 정보는 0또는 1로 이루어진 N개의 숫자로 나타내어지며 공백을 사이에 두고 주어집니다.

# 3 ≤ N ≤ 20
# 출력 형식
# N * N 격자를 벗어나지 않으면서, 3 * 3 크기 격자 내에 들어올 수 있는 최대 동전의 수를 출력해주세요.

# 입출력 예제
# 예제1
# 입력:

# 3
# 1 0 1
# 0 1 0
# 0 1 0
# 출력:

# 4
# 예제2
# 입력:

# 5
# 0 0 0 1 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 0 1 0
# 0 0 0 1 1
# 출력:

# 6
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
grid=[]
for _ in range(n):
    grid.append(list(map(int, input().split())))
def get_coin(y, x, cnt):
    for k in range(y, y+3):
        for l in range(x, x+3):
            cnt+=grid[k][l]
    return cnt
answer=0
for i in range(n):
    for j in range(n):
        if i+2<n and j+2<n:
            answer=max(answer, get_coin(i, j, 0))
print(answer)
