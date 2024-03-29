# 놀이기구 탑승
# 쉬움
# 정답률 36%

# ·
# 제출 223회

# ·
# 예상 소요 시간 74분


# Like
# 추천해요
# Dislike
# 아쉬워요

# ko-kr

# n * n 명의 학생을 다음과 같이 n * n 크기의 격자 모양으로 생긴 놀이기구에 순서대로 탑승시키려고 합니다. 처음에는 놀이기구의 모든 칸이 비어져있습니다. (r, c)는 r행 c열을 의미합니다.



# 이때 각 학생별로 좋아하는 학생이 정확히 4명씩 정해져 있습니다. 자기 자신을 좋아하는 학생은 없고, 동일한 학생에 대해 좋아하는 학생의 번호가 중복하여 주어지는 경우도 없습니다.



# 이때 학생들은, 입력으로 주어진 순서대로 다음 조건에 따라 가장 우선순위가 높은 칸으로 탑승하려고 합니다. 단, 항상 비어있는 칸으로만 이동합니다.

# 격자를 벗어나지 않는 4방향으로 인접한 칸 중 앉아있는 좋아하는 친구의 수가 가장 많은 위치로 갑니다.

# 만약 1번 조건을 만족하는 칸의 위치가 여러 곳이라면, 그 중 인접한 칸 중 비어있는 칸의 수가 가장 많은 위치로 갑니다. 단 이때 격자를 벗어나는 칸은 비어있는 칸으로 간주하지 않습니다.

# 만약 2번 조건까지 동일한 위치가 여러 곳이라면, 그 중 행 번호가 가장 작은 위치로 갑니다.

# 만약 3번 조건까지 동일한 위치가 여러 곳이라면, 그 중 열 번호가 가장 작은 위치로 갑니다.

# 위의 조건 하에 실제 시뮬레이션을 진행해보면 다음과 같습니다. 먼저 3번 학생은, 비어 있는 칸의 수가 4개인 (2, 2) 위치로 들어가게 됩니다.



# 다음 6번 학생은, 인접한 곳에 좋아하는 학생의 수가 1명인 (1, 2), (2, 1), (2, 3), (3, 2) 칸들을 살펴봅니다. 이 칸들은 전부 인접한 곳에 비어있는 칸의 수가 2개로 동일하기 때문에, 그 중 행 번호가 가장 작은 (1, 2) 위치로 들어가게 됩니다.



# 다음 1번 학생은, 인접한 곳에 좋아하는 학생의 수가 1명인 (1, 1), (1, 3) 칸들을 살펴봅니다. 이 칸들은 전부 인접한 곳에 비어있는 칸의 수가 1개로 동일하며 행 번호 역시 1로 동일하기 때문에, 그 중 열 번호가 가장 작은 위치인 (1, 1)로 이동합니다.



# 다음 8번 학생은, 인접한 곳에 좋아하는 학생 수가 2명인 유일한 칸인 (2, 1)로 이동하게 됩니다.



# 학생들이 전부 탑승한 이후의 상태는 다음과 같습니다.



# 이때 최종 점수는 모든 학생들이 탑승한 이후, 각 학생마다의 점수를 합한 점수가 됩니다. 각 학생의 점수는 해당 학생의 인접한 곳에 앉아 있는 좋아하는 친구의 수로 결정됩니다.



# 예를 들어 위의 경우에서 1번 학생의 경우 인접한 곳에 좋아하는 친구가 6번, 8번 이렇게 2명 있으므로, 10점을 얻게 됩니다. 최종 점수는 탑승하는 순서대로 10 + 100 + 10 + 10 + 10 + 10 + 10 + 10 + 0 = 170이 됩니다.

# 들어오는 학생의 순서와 각 학생마다 좋아하는 4명의 학생 번호가 주어졌을 때, 최종 점수를 구하는 프로그램을 작성해보세요.

# 입력 형식
# 첫 번째 줄에는 격자의 크기를 나타내는 n이 주어집니다.

# 두 번째 줄부터는 n * n개의 줄에 걸쳐 각 학생의 정보 n0, n1, n2, n3, n4가 각각 공백을 사이에 주어집니다. n0는 지금 턴에 탑승하는 학생의 번호, n1, n2, n3, n4는 n0 학생이 좋아하는 학생의 번호를 나타냅니다. n0, n1, n2, n3, n4는 전부 다른 숫자이며, 1에서 n * n사이의 숫자임을 가정해도 좋습니다. 또한, n * n개의 줄에 걸쳐 주어지는 n0는 서로 겹치지 않음을 가정해도 좋습니다.

# 3 ≤ n ≤ 20
# 출력 형식
# 모든 학생들이 놀이기구에 탑승한 이후의 최종 점수를 출력합니다.

# 입출력 예제
# 예제1
# 입력:

# 3
# 3 5 8 9 2
# 6 1 2 3 4
# 1 5 8 7 6
# 8 2 5 3 1
# 9 4 8 2 1
# 4 6 5 7 8
# 7 3 4 2 9
# 2 1 6 3 5
# 5 4 3 8 6
# 출력:

# 170
# 예제2
# 입력:

# 3
# 3 5 8 9 2
# 6 1 2 3 4
# 1 5 8 7 6
# 8 2 5 3 1
# 9 4 8 2 1
# 4 6 5 7 8
# 7 3 4 2 9
# 2 1 9 3 5
# 5 4 3 2 7
# 출력:

# 270
# 제한
# 시간 제한: 1000ms
# 메모리 제한: 80MB
n=int(input())
student=[[] for _ in range(n**2+1)]
seat=[[0 for _ in range(n)] for _ in range(n)]
dy, dx=[0, 1, 0, -1], [1, 0, -1, 0]
def get_total():
    total=0
    for i in range(n):
        for j in range(n):
            cnt=0
            for k in range(4):
                ni, nj=i+dy[k], j+dx[k]
                if 0<=ni<n and 0<=nj<n and seat[ni][nj] in set(student[seat[i][j]]):
                    cnt+=1
            if cnt==0:
                continue
            else:
                total+=10**(cnt-1)
    return total
for i in range(n**2):
    n0, n1, n2, n3, n4=map(int, input().split())
    student[n0]=[n1, n2, n3, n4]
    if i==0:
        seat[1][1]=n0
    else:
        tmp=[]
        for i in range(n):
            for j in range(n):
                like=0
                zero=0
                if seat[i][j]==0:
                    for k in range(4):
                        ni, nj=i+dy[k], j+dx[k]
                        if 0<=ni<n and 0<=nj<n:
                            if seat[ni][nj]==0:
                                zero+=1
                            elif seat[ni][nj] in set(student[n0]):
                                like+=1
                    tmp.append((i, j, like, zero))
        tmp.sort(key=lambda x:(x[2], x[3]), reverse=True)
        ny, nx, _, _=tmp[0]
        seat[ny][nx]=n0
print(get_total())
