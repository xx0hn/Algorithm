# 양수 직사각형의 최대 크기
# n * m크기의 이차원 영역의 각 위치에 정수 값이 하나씩 적혀있습니다. 이 영역 안에서 가능한 양수 직사각형 중 최대 크기를 구하려고 합니다. 양수 직사각형이란, 직사각형의 변들이 주어진 격자 판에 평행하면서, 직사각형 내에 있는 숫자들이 전부 양수인 직사각형을 의미합니다. 최대 크기의 양수 직사각형을 찾는 프로그램을 작성해보세요.

# 예를 들어 다음 그림의 경우에는, 크기가 6인 양수 직사각형을 찾을 수 있습니다.



# 입력 형식
# 첫 번째 줄에는 n과 m이 공백을 사이에 두고 주어지고, 두 번째 줄부터 (n+1)번째 줄까지는 각 행의 숫자가 공백을 사이에 두고 주어집니다.

# 1 ≤ n, m ≤ 20

# -1,000 ≤ 정수 값 ≤ 1,000

# 출력 형식
# 모든 값이 양수로만 이루어져 있는 직사각형 중 최대 크기를 출력해주세요. 만약 그러한 직사각형이 없다면, -1을 출력해주세요.

# 입출력 예제
# 예제1
# 입력:

# 3 3
# 1 2 3
# 3 4 5
# 6 7 8
# 출력:

# 9
# 예제2
# 입력:

# 4 5
# 6 -2 4 -3 1
# 3 6 7 -4 1
# 6 1 8 15 -5
# 3 -5 1 16 3
# 출력:

# 6
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n, m=map(int, input().split())
grid=[list(map(int, input().split())) for _ in range(n)]
def find_sq(y, x, h, w):
    result=0
    if y+h>=n or x+w>=m:
        return 0
    for i in range(y, y+h+1):
        for j in range(x, x+w+1):
            if grid[i][j]<=0:
                return 0
            else:
                result+=1
    return result
answers=[]
for i in range(n):
    for j in range(m):
        for k in range(n):
            for l in range(m):
                answers.append(find_sq(i, j, k, l))
answer=max(answers)
if not answer:
    print(-1)
else:
    print(answer)
