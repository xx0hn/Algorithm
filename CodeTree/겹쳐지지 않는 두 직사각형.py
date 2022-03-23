# 겹쳐지지 않는 두 직사각형
# n * m크기의 이차원 영역의 각 위치에 정수 값이 하나씩 적혀있습니다. 이 영역 안에서 서로 겹치지 않는 두 직사각형을 적절하게 잡아, 두 직사각형 안에 적힌 숫자들의 총 합을 최대로 하는 프로그램을 작성해보세요. 이때, 각 직사각형의 변들은 격자 판에 평행해야 하고 꼭 2개의 직사각형을 골라야만 하며, 두 직사각형의 경계는 서로 닿아도 됩니다.

# 예를 들어 다음 그림의 경우에는, 두 직사각형을 적절히 잡아 합을 62 만큼 만들 수 있습니다.



# 입력 형식
# 첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고, 두 번째 줄부터 (n+1)번째 줄까지는 각 행의 숫자가 공백을 사이에 두고 주어집니다.

# 2 ≤ n, m ≤ 5

# -1,000 ≤ 정수 값 ≤ 1,000

# 출력 형식
# 겹치지 않게 두 직사각형을 잡았을 때, 얻을 수 있는 최대 합을 출력해주세요.

# 입출력 예제
# 예제1
# 입력:

# 2 2
# -1 -2
# -3 -4
# 출력:

# -3
# 예제2
# 입력:

# 4 5
# 6 5 4 -3 1
# 3 -4 -4 14 1
# 6 1 -3 15 -5
# 3 -5 1 16 3
# 출력:

# 63
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
chk=[[0]*m for _ in range(n)]
answers=[]
def find_sq(y1, x1, y2, x2):
    result=0
    for i in range(y1, y2+1):
        for j in range(x1, x2+1):
            chk[i][j]+=1
            result+=grid[i][j]
    return result
def chk_sq():
    for i in range(n):
        for j in range(m):
            if chk[i][j]>=2:
                return False
    return True
def init_chk():
    for i in range(n):
        for j in range(m):
            chk[i][j]=0
def get_sum(y1, x1, y2, x2):
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    init_chk()
                    sq1=find_sq(y1, x1, y2, x2)
                    sq2=find_sq(i, j, k, l)
                    if chk_sq():
                        answers.append(sq1+sq2)
for i in range(n):
    for j in range(m):
        for k in range(i, n):
            for l in range(j, m):
                get_sum(i, j, k, l)
print(max(answers))
